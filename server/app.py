import sys
from fastapi import FastAPI
import uvicorn

# FORCE LOGS TO APPEAR
print(">>> SERVER IS STARTING <<<", flush=True)
sys.stdout.flush()

try:
    from env import BrowserOrganizerEnv
    env = BrowserOrganizerEnv()
    print(">>> ENVIRONMENT LOADED <<<", flush=True)
except Exception as e:
    print(f">>> ERROR: {e} <<<", flush=True)

app = FastAPI()

@app.get("/")
async def health():
    return {"status": "ok"}

@app.post("/reset")
async def reset():
    print(">>> RESET CALLED BY GRADER <<<", flush=True)
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