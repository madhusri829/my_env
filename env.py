import gymnasium as gym
from gymnasium import spaces
import numpy as np
from datetime import datetime

class BrowserOrganizerEnv(gym.Env):
    def __init__(self, render_mode=None):
        super(BrowserOrganizerEnv, self).__init__()
        self.action_space = spaces.Discrete(12)
        
        self.data = [
            {"title": "Python Tutorial", "url": "https://docs.python.org", "date": "2026-03-01", "usage_count": {"study": 20, "movies": 0}},
            {"title": "Win Free Money", "url": "http://scam-site.biz/scam", "date": "2026-03-05", "usage_count": {"others": 1}},
            {"title": "Hackathon Submission", "url": "https://devpost.com/hack", "date": "2026-02-15", "usage_count": {"hackathon": 50}},
            {"title": "Action Movies", "url": "https://youtube.com/movies", "date": "2026-01-10", "usage_count": {"movies": 15}}
        ]
        self.current_index = 0

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)
        self.current_index = 0
        observation = self.data[self.current_index]
        return observation, {}

    def step(self, action):
        # Basic reward logic
        item = self.data[self.current_index]
        reward = 1 if action == 0 else 0 
        
        self.current_index += 1
        terminated = self.current_index >= len(self.data)
        truncated = False
        
        if not terminated:
            observation = self.data[self.current_index]
        else:
            observation = self.data[self.current_index - 1]

        return observation, reward, terminated, truncated, {}