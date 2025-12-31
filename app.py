from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
import datetime

app = FastAPI()

# Enable CORS so your HTML can talk to this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", response_class=HTMLResponse)
async def get_index():
    # Place your entire HTML code inside the return
    with open("spin.html", "r", encoding="utf-8") as f:
        return f.read()

@app.post("/api/claim-reward")
async def claim_reward(info: dict):
    # This will highlight her choice in your Render Logs
    gift = info.get("gift_chosen", "Unknown")
    
    print("\n" + "⭐" * 40)
    print(f"BIRTHDAY SURPRISE LOG")
    print(f"CHOICE MADE: {gift}")
    print(f"TIME: {info.get('timestamp')}")
    print("⭐" * 40 + "\n")
    
    return {"status": "success", "choice_received": gift}