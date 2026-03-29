from fastapi import FastAPI
import uvicorn
from env import BrowserOrganizerEnv

# This will show up in your logs immediately
print("--- STARTING OPENENV SERVER ---")

app = FastAPI()
env = BrowserOrganizerEnv()

@app.get("/")
async def health():
    return {"status": "online"}

@app.post("/reset")
async def reset():
    print("Grader called RESET")
    obs, info = env.reset()
    return {"observation": obs, "info": info}

@app.post("/step")
async def step(request: dict):
    action = request.get("action", 0)
    obs, reward, terminated, truncated, info = env.step(action)
    return {
        "observation": obs,
        "reward": reward,
        "terminated": terminated,
        "truncated": truncated,
        "info": info
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)