import gymnasium as gym
from gymnasium import spaces

class BrowserOrganizerEnv(gym.Env):
    def __init__(self, render_mode=None):
        super().__init__()
        self.action_space = spaces.Discrete(12)
        
        # FEATURE: User-registered contests for reminders
        self.data = [
            {"title": "Codeforces Round 900", "url": "https://codeforces.com", "registered": True, "category": "hackathon"},
            {"title": "LeetCode Weekly 400", "url": "https://leetcode.com", "registered": True, "category": "hackathon"},
            {"title": "Python for Data Science", "url": "https://coursera.org", "registered": False, "category": "study"}
        ]
        self.current_index = 0

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)
        self.current_index = 0
        return self.data[self.current_index], {}

    def step(self, action):
        item = self.data[self.current_index]
        reward = 0
        
        # LOGIC: Reward for contest reminders (Action 11)
        if item.get("registered"):
            if action == 11: 
                reward = 20  # Bonus for reminding scheduled contest
                print(f">>> REMINDER SENT: {item['title']}")
            else: 
                reward = -10 # Penalty for missing it
        elif action == 0 and item["category"] == "study":
            reward = 5
            
        self.current_index += 1
        terminated = self.current_index >= len(self.data)
        
        obs = self.data[self.current_index if not terminated else self.current_index - 1]
        return obs, reward, terminated, False, {}