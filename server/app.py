import os
import sys
from fastapi import FastAPI
import uvicorn

# This line MUST show up in logs if the server starts
print(">>> SERVER BOOT SEQUENCE STARTED <<<", flush=True)

try:
    from env import BrowserOrganizerEnv
    print(">>> ENV.PY LOADED SUCCESSFULLY <<<", flush=True)
except Exception as e:
    print(f">>> ERROR LOADING ENV.PY: {e} <<<", flush=True)

app = FastAPI()
env = BrowserOrganizerEnv()

@app.get("/")
async def root():
    return {"message": "OpenEnv Server Running"}

@app.post("/reset")
async def reset():
    print(">>> GRADER CALLED RESET <<<", flush=True)
    obs, info = env.reset()
    return {"observation": obs, "info": info}

@app.post("/step")
async def step(data: dict):
    action = data.get("action", 0)
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