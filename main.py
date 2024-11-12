import time
import os
import json
from datetime import datetime, timedelta
from reddit_scraper.reddit_scraper import get_hottest_posts, rewrite_post_for_tweet
from tweet_scheduler.tweet_scheduler import schedule_tweet

subreddits = ['sui', 'CryptoCurrency', 'Bitcoin', 'CryptoMoonShots', 'Ethereum', 'dogecoin', 'solana','Altcoin', 'cryptocurrencymemes', 'defi', 'SatoshiStreetBets']
ETZ_LINK = ""
LAST_POSTS_FILE = 'last_posts.json'
SUBREDDIT_INDEX_FILE = 'subreddit_index.json'

def load_last_posts():
    if os.path.exists(LAST_POSTS_FILE):
        with open(LAST_POSTS_FILE, 'r') as f:
            return json.load(f)
    return {subreddit: None for subreddit in subreddits}

def save_last_posts(last_posts):
    with open(LAST_POSTS_FILE, 'w') as f:
        json.dump(last_posts, f)

def load_subreddit_index():
    if os.path.exists(SUBREDDIT_INDEX_FILE):
        with open(SUBREDDIT_INDEX_FILE, 'r') as f:
            data = json.load(f)
            if isinstance(data, dict) and 'index' in data:
                return data['index']
            elif isinstance(data, int):
                return data
    return 0

def save_subreddit_index(index):
    with open(SUBREDDIT_INDEX_FILE, 'w') as f:
        json.dump({'index': index}, f)

def log_post_details(post):
    print("Title:", post['title'])
    print("Post URL:", post['post_url'])
    print("Content URL:", post['url'])
    print("Selftext:", post['selftext'])
    print("Comments:", post['comments'])
    print("Media Links:", post['media_links'])
    print("Created At:", post['created_utc'])
    print("-------------------------")

def job():
    print("Starting job...")
    last_posts = load_last_posts()
    subreddit_index = load_subreddit_index()
    subreddit = subreddits[subreddit_index % len(subreddits)]
    print(f"Using subreddit: r/{subreddit}")
    save_subreddit_index((subreddit_index + 1) % len(subreddits))

    last_post_time = last_posts.get(subreddit, None)
    if last_post_time:
        last_post_time = datetime.fromtimestamp(last_post_time)
    else:
        last_post_time = datetime.now() - timedelta(days=1)

    print(f"Fetching posts for r/{subreddit} after {last_post_time}")

    # Get more posts to filter through
    posts = get_hottest_posts(subreddit, limit=10, after=last_post_time)
    if not posts:
        print(f"No posts found for subreddit: r/{subreddit}")
        return

    # Filter for posts with media links
    media_posts = [post for post in posts if post['media_links']]
    if not media_posts:
        print(f"No posts with media found for subreddit: r/{subreddit}")
        return

    post = media_posts[0]  # Take the highest ranked post with media
    log_post_details(post)
    tweet = rewrite_post_for_tweet(post['title'], post['url'], post['selftext'], post['comments'], subreddit, post['post_url'])
    if tweet == "Error generating tweet":
        print("Error in generating tweet, skipping...")
        return

    tweet_with_link = f"{tweet}\n\n{ETZ_LINK}"
    print("Final Tweet Thread:", tweet_with_link)

    try:
        schedule_tweet(tweet_with_link, post['media_links'])
        last_posts[subreddit] = post['created_utc']
        save_last_posts(last_posts)
    except Exception as e:
        print(f"Failed to schedule tweet thread: {e}")

if __name__ == "__main__":
    print("Running script...")
    job()
    print("Script finished.")
