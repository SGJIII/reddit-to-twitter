from main import job, subreddits, load_subreddit_index
from tweet_scheduler.tweet_scheduler import schedule_tweet

def run_next_job(test_mode=True):
    """Run the next job and show which subreddit it's using"""
    current_index = load_subreddit_index()
    current_subreddit = subreddits[current_index % len(subreddits)]
    print(f"\nRunning job for subreddit {current_index + 1}/{len(subreddits)}: r/{current_subreddit}")
    
    if test_mode:
        # Store original function
        original_schedule_tweet = schedule_tweet
        
        try:
            # Override with test mode
            def test_schedule_tweet(tweet_content, **kwargs):
                return original_schedule_tweet(tweet_content, test_mode=True)
            import main
            main.schedule_tweet = test_schedule_tweet
            
            # Run the job
            job()
            
        finally:
            # Restore original function
            main.schedule_tweet = original_schedule_tweet
    else:
        # Run real job
        job()

if __name__ == "__main__":
    # Show current position in rotation
    current_index = load_subreddit_index()
    print(f"Current subreddit index: {current_index}")
    print(f"Subreddits rotation: {subreddits}")
    
    while True:
        choice = input("\nOptions:\n1. Run next job (test mode)\n2. Run next job (REAL post)\n3. Show current position\n4. Exit\nChoice: ")
        
        if choice == "1":
            run_next_job(test_mode=True)
        elif choice == "2":
            confirm = input("This will post a REAL tweet. Are you sure? (y/n): ")
            if confirm.lower() == 'y':
                run_next_job(test_mode=False)
        elif choice == "3":
            current_index = load_subreddit_index()
            current_subreddit = subreddits[current_index % len(subreddits)]
            print(f"\nCurrent position: {current_index + 1}/{len(subreddits)}")
            print(f"Next subreddit will be: r/{current_subreddit}")
        elif choice == "4":
            break
        else:
            print("Invalid choice") 