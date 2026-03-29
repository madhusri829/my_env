import gymnasium as gym
from gymnasium import spaces

class BrowserOrganizerEnv(gym.Env):
    def __init__(self, render_mode=None):
        super(BrowserOrganizerEnv, self).__init__()
        self.action_space = spaces.Discrete(12)
        
        # Data includes 'is_registered' for contests
        self.data = [
            {"title": "Codeforces Round 900", "url": "https://codeforces.com", "is_registered": True, "category": "hackathon"},
            {"title": "LeetCode Weekly", "url": "https://leetcode.com", "is_registered": True, "category": "hackathon"},
            {"title": "Python Basics", "url": "https://docs.python.org", "is_registered": False, "category": "study"}
        ]
        self.current_index = 0

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)
        self.current_index = 0
        return self.data[self.current_index], {}

    def step(self, action):
        item = self.data[self.current_index]
        reward = 0
        
        # Logic for Contest Reminders
        if item.get("is_registered") == True:
            if action == 11: reward += 20 # High reward for reminder
            else: reward -= 10
        elif action == 0 and item["category"] == "study": reward += 5
        
        self.current_index += 1
        done = self.current_index >= len(self.data)
        obs = self.data[self.current_index if not done else self.current_index-1]
        
        return obs, reward, done, False, {}