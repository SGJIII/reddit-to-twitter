import requests
import config

def schedule_tweet(tweet_content, twitter_options=None):
    url = "https://app.ayrshare.com/api/post"
    payload = {
        "post": tweet_content,
        "platforms": ["twitter"],
    }

    if twitter_options:
        payload["twitterOptions"] = twitter_options

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {config.AYRSHARE_API_KEY}"
    }

    response = requests.post(url, json=payload, headers=headers)
    if response.status_code != 200:
        raise Exception(f"Failed to schedule tweet: {response.json()}")
    else:
        print("Tweet scheduled successfully:", response.json())
