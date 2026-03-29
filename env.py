import gymnasium as gym
from gymnasium import spaces
import numpy as np

class BrowserOrganizerEnv(gym.Env):
    def __init__(self, render_mode=None):
        super(BrowserOrganizerEnv, self).__init__()
        # 12 Actions as defined in your problem statement
        self.action_space = spaces.Discrete(12)
        
        self.data = [
            {"title": "Python Tutorial", "url": "https://docs.python.org", "date": "2026-03-01", "usage_count": {"study": 20}},
            {"title": "Win Free Money", "url": "http://scam-site.biz/scam", "date": "2026-03-05", "usage_count": {"others": 1}},
            {"title": "Hackathon Submission", "url": "https://devpost.com/hack", "date": "2026-02-15", "usage_count": {"hackathon": 50}}
        ]
        self.current_index = 0

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)
        self.current_index = 0
        # Return observation and empty info dict
        observation = self.data[self.current_index]
        return observation, {}

    def step(self, action):
        # Reward logic: +5 for correct category (0=study, 1=hackathon, 7=harmful)
        item = self.data[self.current_index]
        reward = 0
        
        if action == 0 and "Python" in item['title']: reward = 5
        if action == 7 and "http://" in item['url']: reward = 10
        
        self.current_index += 1
        terminated = self.current_index >= len(self.data)
        truncated = False
        
        if not terminated:
            observation = self.data[self.current_index]
        else:
            observation = self.data[self.current_index - 1]

        # Return 5 values: obs, reward, terminated, truncated, info
        return observation, reward, terminated, truncated, {}