from reddit_scraper.reddit_scraper import get_hottest_posts
from tweet_scheduler.tweet_scheduler import schedule_tweet
from main import job

def test_single_subreddit(subreddit_name):
    print(f"\nTesting subreddit: r/{subreddit_name}")
    print("=" * 50)
    
    # Get posts
    posts = get_hottest_posts(subreddit_name, limit=10)
    
    # Show all posts with external links
    print(f"\nFound {len(posts)} posts with external links:")
    for i, post in enumerate(posts, 1):
        print(f"\nPost {i}:")
        print(f"Title: {post['title']}")
        print(f"External URL: {post['url']}")
        print(f"Post URL: {post['post_url']}")
        print("-" * 30)

def test_full_job():
    print("\nTesting full job execution")
    print("=" * 50)
    job()

if __name__ == "__main__":
    # Test specific subreddits
    subreddits_to_test = ['CryptoCurrency', 'Bitcoin', 'dogecoin']
    
    for subreddit in subreddits_to_test:
        test_single_subreddit(subreddit)
    
    # Uncomment to test the full job
    # test_full_job()