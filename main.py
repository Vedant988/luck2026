from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from datetime import datetime
import os

app = FastAPI()

# CORS middleware for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ClaimRequest(BaseModel):
    status: str
    gift: str

# Store claims (in production, use a database)
claims = []

@app.get("/", response_class=HTMLResponse)
async def read_root():
    """Serve the frontend HTML"""
    # In production, replace this with your actual HTML file path
    try:
        with open("spin.html", "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return """
        <h1>Frontend not found</h1>
        <p>Please ensure spin.html is in the same directory as main.py</p>
        """

@app.post("/api/claim-reward")
async def claim_reward(request: ClaimRequest):
    """Handle reward claim - This is where you'll see the flag!"""
    
    claim_data = {
        "status": request.status,
        "gift": request.gift,
        "timestamp": datetime.now().isoformat(),
        "flag": "🎉 PRANK_SUCCESSFUL! She clicked the button! 🎁"
    }
    
    claims.append(claim_data)
    
    # Print to console so you can see it in Render logs
    print("\n" + "="*50)
    print("🎊 REWARD CLAIMED! 🎊")
    print(f"Status: {request.status}")
    print(f"Gift: {request.gift}")
    print(f"Time: {claim_data['timestamp']}")
    print("FLAG: 🎉 PRANK_SUCCESSFUL! She clicked the button! 🎁")
    print("="*50 + "\n")
    
    return {
        "success": True,
        "message": "Reward claimed successfully",
        "order_id": f"LRC{int(datetime.now().timestamp())}",
        "flag": claim_data["flag"]
    }

@app.get("/api/claims")
async def get_claims():
    """View all claims - your secret endpoint to check if she fell for it"""
    return {
        "total_claims": len(claims),
        "claims": claims
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)