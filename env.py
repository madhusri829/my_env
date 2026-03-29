import gymnasium as gym
from gymnasium import spaces
import numpy as np
from datetime import datetime

class BrowserOrganizerEnv(gym.Env):
    def __init__(self, render_mode=None):
        super(BrowserOrganizerEnv, self).__init__()

        # Actions: 0-4: Categories, 5: Remove, 6: Safe, 7: Harmful, 8: Group, 9: Month, 10: Usage, 11: Reminder
        self.action_space = spaces.Discrete(12)
        
        # Observation space is a dictionary (OpenEnv handles this automatically)
        # We define a placeholder here for compatibility
        self.observation_space = spaces.Dict({})

        # The Data your AI will organize
        self.data = [
            {"title": "Advanced Python Patterns", "url": "https://docs.python.org", "date": "2026-03-01", "usage_count": {"study": 20, "movies": 0}},
            {"title": "Get Rich Quick! Click Here", "url": "http://scam-site.biz/scam", "date": "2026-03-05", "usage_count": {"others": 1}},
            {"title": "Hackathon Final Submission", "url": "https://devpost.com/hack", "date": "2026-02-15", "usage_count": {"hackathon": 50}},
            {"title": "Avengers: Secret Wars Trailer", "url": "https://youtube.com/marvel", "date": "2026-01-10", "usage_count": {"movies": 15}},
            {"title": "Duplicate Movie Link", "url": "https://youtube.com/duplicate", "date": "2026-01-11", "usage_count": {"movies": 1}}
        ]
        
        self.current_index = 0
        self.state = self.data[self.current_index]

    def reset(self, seed=None, options=None):
        # REQUIRED for Gymnasium: Initialize the random seed
        super().reset(seed=seed)
        
        self.current_index = 0
        self.state = self.data[self.current_index]
        
        # FIXED: Returns observation AND empty info dictionary (2 values)
        return self.state, {}

    def _calculate_reward(self, action):
        item = self.state
        reward = 0
        
        # Category Logic (Actions 0-4)
        if action == 0 and "python" in item['title'].lower(): reward += 5
        elif action == 1 and "hackathon" in item['title'].lower(): reward += 5
        elif action == 3 and "avengers" in item['title'].lower(): reward += 5
        
        # Harmful Detection (Action 7)
        elif action == 7:
            if "http://" in item['url'] or "scam" in item['url']: 
                reward += 10 # Correctly identified harm
            else: 
                reward -= 10 # False alarm

        # Reminder Logic (Action 11)
        elif action == 11:
            most_used = max(item['usage_count'], key=item['usage_count'].get)
            if most_used in ["study", "hackathon"]: reward += 6
            else: reward -= 5

        # Small penalty for unnecessary actions
        else:
            reward -= 1
            
        return reward

    def step(self, action):
        reward = self._calculate_reward(action)
        
        self.current_index += 1
        
        # 'terminated' is True when we finish the dataset
        terminated = self.current_index >= len(self.data)
        truncated = False # Not used for this simple environment
        
        if not terminated:
            self.state = self.data[self.current_index]
        else:
            # Stay on the last item if done to avoid index errors
            self.state = self.data[self.current_index - 1]

        # FIXED: Returns 5 values (observation, reward, terminated, truncated, info)
        return self.state, reward, terminated, truncated, {}

    def render(self):
        print(f"Current State: {self.state['title']}")