import gym
from gym import spaces
import numpy as np
from datetime import datetime

class BrowserOrganizerEnv(gym.Env):
    def __init__(self):
        super(BrowserOrganizerEnv, self).__init__()

        # Actions: 0-4: Categories, 5: Remove, 6: Safe, 7: Harmful, 8: Group, 9: Month, 10: Usage, 11: Reminder
        self.action_space = spaces.Discrete(12)
        
        # Mock dataset: In a real scenario, this would be a large JSON/Database
        self.data = [
            {"title": "Advanced Python Patterns", "url": "https://docs.python.org", "date": "2026-03-01", "usage_count": {"study": 20, "movies": 0}},
            {"title": "Get Rich Quick! Click Here", "url": "http://malicious-site.biz/scam", "date": "2026-03-05", "usage_count": {"others": 1}},
            {"title": "Hackathon Final Submission", "url": "https://devpost.com/hack", "date": "2026-02-15", "usage_count": {"hackathon": 50}},
            {"title": "Avengers: Secret Wars Trailer", "url": "https://youtube.com/marvel", "date": "2026-01-10", "usage_count": {"movies": 15}},
            {"title": "Duplicate Movie Link", "url": "https://youtube.com/marvel", "date": "2026-01-11", "usage_count": {"movies": 1}}
        ]
        
        self.current_index = 0
        self.state = self.data[self.current_index]

    def reset(self):
        self.current_index = 0
        self.state = self.data[self.current_index]
        return self.state

    def _calculate_reward(self, action):
        item = self.state
        reward = 0
        
        # 0-4: Classification logic
        if action == 0 and "python" in item['title'].lower(): reward += 5
        elif action == 1 and "hackathon" in item['title'].lower(): reward += 5
        elif action == 3 and "avengers" in item['title'].lower(): reward += 5
        
        # 7: Harmful Detection
        elif action == 7:
            if "http://" in item['url'] or "scam" in item['url']: reward += 10
            else: reward -= 10 # Penalize marking safe content as harmful

        # 9: Month Assignment
        elif action == 9:
            month = datetime.strptime(item['date'], "%Y-%m-%d").strftime("%B")
            if (month == "March" and "03" in item['date']) or (month == "February" and "02" in item['date']):
                reward += 5

        # 11: Reminder Logic
        elif action == 11:
            most_used = max(item['usage_count'], key=item['usage_count'].get)
            if most_used in ["study", "hackathon"]: reward += 6
            else: reward -= 5

        # General "Wrong Action" penalty
        else:
            reward -= 2
            
        return reward

    def step(self, action):
        reward = self._calculate_reward(action)
        
        self.current_index += 1
        done = self.current_index >= len(self.data)
        
        if not done:
            self.state = self.data[self.current_index]
        else:
            self.state = None

        return self.state, reward, done, {}