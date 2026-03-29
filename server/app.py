# 1. PRINT IMMEDIATELY (Before imports)
print("!!! DEBUG: SERVER ATTEMPTING TO START !!!")

import os
import sys

# 2. PRINT THE PATHS (Helps us see if files are missing)
print(f"Current Directory: {os.getcwd()}")
print(f"Files in directory: {os.listdir('.')}")

try:
    from fastapi import FastAPI
    import uvicorn
    from env import BrowserOrganizerEnv
    print("!!! DEBUG: ALL LIBRARIES IMPORTED SUCCESSFULLY !!!")
except Exception as e:
    print(f"!!! DEBUG: IMPORT ERROR: {e} !!!")
    sys.exit(1)

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
    print("!!! DEBUG: STARTING UVICORN ON PORT 8000 !!!")
    uvicorn.run(app, host="0.0.0.0", port=8000)