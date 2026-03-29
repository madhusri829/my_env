import gymnasium as gym
from gymnasium import spaces
import numpy as np
from datetime import datetime

class BrowserOrganizerEnv(gym.Env):
    def __init__(self, render_mode=None):
        super(BrowserOrganizerEnv, self).__init__()
        self.action_space = spaces.Discrete(12)
        
        # ADDED: Registration and Scheduling info in the data
        self.data = [
            {
                "title": "Codeforces Global Round 25", 
                "url": "https://codeforces.com/contest/123", 
                "is_registered": True, # User signed up!
                "event_time": "2026-03-30 18:00",
                "category": "hackathon"
            },
            {
                "title": "LeetCode Weekly Contest", 
                "url": "https://leetcode.com/contest", 
                "is_registered": True, 
                "event_time": "2026-03-31 08:00",
                "category": "hackathon"
            },
            {
                "title": "Python Tutorial", 
                "url": "https://docs.python.org", 
                "is_registered": False, 
                "event_time": None,
                "category": "study"
            }
        ]
        self.current_index = 0

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)
        self.current_index = 0
        observation = self.data[self.current_index]
        return observation, {}

    def _calculate_reward(self, action):
        item = self.data[self.current_index]
        reward = 0
        
        # NEW LOGIC: Scheduling Reminder
        if item.get("is_registered") == True:
            if action == 11: # send_reminder
                reward += 20  # High reward for reminding about a registered contest!
                print(f"✅ AI reminded user about: {item['title']}")
            else:
                reward -= 15  # Heavy penalty for forgetting a registered event!
        
        # Category Logic
        elif action == 0 and item["category"] == "study": reward += 5
        elif action == 1 and item["category"] == "hackathon": reward += 5
            
        return reward

    def step(self, action):
        reward = self._calculate_reward(action)
        self.current_index += 1
        terminated = self.current_index >= len(self.data)
        truncated = False
        
        if not terminated:
            observation = self.data[self.current_index]
        else:
            observation = self.data[self.current_index - 1]

        return observation, reward, terminated, truncated, {}
        print(f"Current State: {self.state['title']}")