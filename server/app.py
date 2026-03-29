import os
from fastapi import FastAPI
import uvicorn
from env import BrowserOrganizerEnv

# STARTUP PRINT FOR LOGS
print("--- SERVER IS STARTING NOW ---")

app = FastAPI()
env = BrowserOrganizerEnv()

@app.get("/")
async def health_check():
    return {"status": "running", "project": "AI-Browser-Organizer"}

@app.post("/reset")
async def reset():
    print("Grader requested a RESET")
    obs, info = env.reset()
    return {"observation": obs, "info": info}

@app.post("/step")
async def step(action_request: dict):
    action = action_request.get("action", 0)
    obs, reward, terminated, truncated, info = env.step(action)
    return {
        "observation": obs,
        "reward": reward,
        "terminated": terminated,