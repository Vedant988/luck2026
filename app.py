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
    # Fix: Changed 'info' to 'data' and matched the key 'gift' used in JS
    gift = data.get("gift", "Unknown Item")
    gift_url = data.get("url", "No Link Provided")
    timestamp = data.get("timestamp", "N/A")

    # This will show up in your Render Logs
    print("\n" + "⭐" * 30)
    print(f"🎉 BIRTHDAY REWARD CLAIMED!")
    print(f"🎁 Item: {gift}")
    print(f"🔗 Link: {gift_url}")
    print(f"📅 Time: {timestamp}")
    print("⭐" * 30 + "\n")

    return {
        "status": "success", 
        "choice_received": gift,
        "message": "Log recorded successfully"
    }