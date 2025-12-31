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
async def claim(data: dict):
    # 1. Extract all values from the 'data' dictionary sent by the frontend
    gift = data.get("gift", "Unknown Item")
    gift_url = data.get("url", "No Link Provided")
    timestamp = data.get("timestamp", "N/A")
    # This is the line that was missing:
    custom_name = data.get("custom_name", "N/A")

    # 2. Print the standard info
    print("\n" + "⭐" * 30)
    print(f"🎉 BIRTHDAY REWARD CLAIMED!")
    print(f"🎁 Item: {gift}")
    print(f"🔗 Link: {gift_url}")
    print(f"📅 Time: {timestamp}")
    
    # 3. Print the prank name if she chose the bracelet
    if gift == "Personalized Bracelet":
        print(f"🔥 ENGRAVING NAME: {custom_name}") # This will show 'Samruddhv'
    
    print("⭐" * 30 + "\n")

    return {
        "status": "success", 
        "choice_received": gift,
        "message": "Log recorded successfully"
    }
    