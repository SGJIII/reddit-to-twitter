import requests
import json
import config

def schedule_tweet(tweet_content, media_paths=None):
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

    if media_paths:
        media_urls = [{"1": media_path} for media_path in media_paths]
        payload["twitterOptions"]["mediaUrls"] = media_urls

    response = requests.post(url, headers=headers, data=json.dumps(payload))

    if response.status_code == 200:
        print("Tweet scheduled successfully:", response.json())
    else:
        print(f"Failed to schedule tweet: {response.status_code} {response.text}")