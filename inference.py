from env import BrowserOrganizerEnv

def run_agent():
    env = BrowserOrganizerEnv()
    
    # FIXED: Gymnasium reset returns (state, info)
    state, info = env.reset()
    
    done = False
    total_score = 0

    print("--- Starting AI Browser Organizer Inference ---")

    while not done:
        # Now 'state' is the dictionary, so 'title' will work!
        print(f"\nAnalyzing: {state['title']}")
        
        # AI Logic
        if "http://" in state['url']:
            action = 7 # mark_harmful
        elif "python" in state['title'].lower():
            action = 0 # study
        elif "hackathon" in state['title'].lower():
            action = 1 # hackathon
        else:
            action = 3 # movies

        # FIXED: Gymnasium step returns 5 values
        state, reward, terminated, truncated, info = env.step(action)
        
        # Update loop status
        done = terminated or truncated
        total_score += reward
        
        print(f"Action Taken: {action} | Reward Earned: {reward}")

    print(f"\n--- Final Score: {total_score} ---")

if __name__ == "__main__":
    run_agent()