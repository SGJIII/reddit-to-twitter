import requests
import json
import config

def schedule_tweet(tweet_content, test_mode=False):
    """
    Schedule a tweet with option for test mode.
    Args:
        tweet_content: The content to tweet
        test_mode: If True, only simulate the tweet without posting
    """
    if test_mode:
        print("\n=== TEST MODE: Tweet Preview ===")
        print("Tweet Content:")
        tweets = tweet_content.split('\n')
        for i, tweet in enumerate(tweets, 1):
            if tweet.strip():  # Only print non-empty lines
                print(f"\nTweet {i}:")
                print("-" * 50)
                print(tweet)
                print(f"Character count: {len(tweet)}")
                if len(tweet) > 280:
                    print("⚠️ WARNING: Tweet exceeds 280 characters!")
        print("\n=== End Test Mode ===")
        return {"status": "test_success", "preview": tweets}

    # Real posting logic
    url = "https://app.ayrshare.com/api/post"
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {config.AYRSHARE_API_KEY}"
    }

    payload = {
        "post": tweet_content,
        "platforms": ["twitter"],
        "twitterOptions": {
            "thread": True,
            "threadNumber": True
        }
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))

    if response.status_code == 200:
        print("Tweet scheduled successfully:", response.json())
    else:
        print(f"Failed to schedule tweet: {response.status_code} {response.text}")