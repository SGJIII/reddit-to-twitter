from reddit_scraper.reddit_scraper import get_hottest_posts, rewrite_post_for_tweet
from tweet_scheduler.tweet_scheduler import schedule_tweet
from main import job

def test_single_subreddit(subreddit_name):
    print(f"\nTesting subreddit: r/{subreddit_name}")
    print("=" * 50)
    
    # Get posts
    posts = get_hottest_posts(subreddit_name, limit=10)
    
    if not posts:
        print(f"No posts with external links found in r/{subreddit_name}")
        return

    # Show all posts with external links and test tweet generation
    print(f"\nFound {len(posts)} posts with external links:")
    for i, post in enumerate(posts, 1):
        print(f"\nPost {i}:")
        print(f"Title: {post['title']}")
        print(f"External URL: {post['url']}")
        print(f"Post URL: {post['post_url']}")
        
        # Generate and test tweet
        tweet = rewrite_post_for_tweet(
            post['title'], 
            post['url'], 
            post['selftext'], 
            post['comments'], 
            subreddit_name,
            post['post_url']
        )
        
        # Test the tweet scheduling
        schedule_tweet(tweet, test_mode=True)
        print("-" * 50)

def test_full_job():
    """Test the full job execution in test mode"""
    print("\nTesting full job execution")
    print("=" * 50)
    
    # Get the original schedule_tweet function
    original_schedule_tweet = schedule_tweet
    
    try:
        # Override schedule_tweet to use test mode
        def test_schedule_tweet(tweet_content, **kwargs):
            return original_schedule_tweet(tweet_content, test_mode=True)
        
        # Temporarily replace the schedule_tweet function
        import main
        main.schedule_tweet = test_schedule_tweet
        
        # Run the job
        job()
    finally:
        # Restore the original function
        main.schedule_tweet = original_schedule_tweet

if __name__ == "__main__":
    # Test specific subreddits
    subreddits_to_test = ['CryptoCurrency', 'Bitcoin', 'dogecoin']
    
    for subreddit in subreddits_to_test:
        test_single_subreddit(subreddit)
    
    # Test the full job
    test_full_job()