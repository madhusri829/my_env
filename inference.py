from env import BrowserOrganizerEnv

def run_agent():
    env = BrowserOrganizerEnv()
    state = env.reset()
    done = False
    total_score = 0

    print("--- Starting AI Browser Organizer Inference ---")

    while not done:
        print(f"\nAnalyzing: {state['title']}")
        
        # Simulated AI logic (In a real submission, this would be an LLM or Model)
        if "http://" in state['url']:
            action = 7 # mark_harmful
        elif "python" in state['title'].lower():
            action = 0 # study
        elif "hackathon" in state['title'].lower():
            action = 1 # hackathon
        else:
            action = 3 # movies

        next_state, reward, done, _ = env.step(action)
        total_score += reward
        
        print(f"Action Taken: {action} | Reward Earned: {reward}")
        state = next_state

    print(f"\n--- Final Score: {total_score} ---")

if __name__ == "__main__":
    run_agent()