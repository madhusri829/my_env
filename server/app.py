from fastapi import FastAPI
import uvicorn
from env import BrowserOrganizerEnv

print(">>> INITIALIZING SERVER...") # This forces a log entry

app = FastAPI()
env = BrowserOrganizerEnv()

# HEALTH CHECK: This fixes the 1-hour wait!
@app.get("/")
async def health():
    return {"status": "alive", "feature": "contest_reminders"}

@app.post("/reset")
async def reset():
    obs, info = env.reset()
    return {"observation": obs, "info": info}

@app.post("/step")
async def step(data: dict):
    action = data.get("action", 0)
    obs, reward, done, trunc, info = env.step(action)
    return {"observation": obs, "reward": reward, "terminated": done, "truncated": trunc, "info": info}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=7860)