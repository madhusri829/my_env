from fastapi import FastAPI
import uvicorn
from env import BrowserOrganizerEnv

app = FastAPI()
env = BrowserOrganizerEnv()

@app.post("/reset")
async def reset():
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
        "truncated": truncated,
        "info": info
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)