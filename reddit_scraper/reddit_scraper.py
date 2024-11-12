import openai
import config
import praw
from datetime import datetime, timedelta

def get_hottest_posts(subreddit_name, limit=10, after=None):
    try:
        print(f"Fetching hottest posts from r/{subreddit_name}...")
        reddit = praw.Reddit(client_id=config.REDDIT_CLIENT_ID,
                             client_secret=config.REDDIT_CLIENT_SECRET,
                             user_agent=config.REDDIT_USER_AGENT)
        subreddit = reddit.subreddit(subreddit_name)
        hottest_posts = []
        now = datetime.utcnow()
        for post in subreddit.hot(limit=100):  # Increased to 100 to have more posts to filter from
            post_time = datetime.utcfromtimestamp(post.created_utc)
            if (now - post_time) <= timedelta(days=1) and not post.stickied:
                if after and post_time <= after:
                    continue
                
                # Extract external links
                external_links = []
                if hasattr(post, 'url') and post.url:
                    if not post.url.startswith(("https://www.reddit.com", "https://i.redd.it", "https://v.redd.it")):
                        external_links.append(post.url)

                # Only add posts that have external links
                if external_links:
                    comments = []
                    post.comments.replace_more(limit=None)
                    for top_level_comment in post.comments[:20]:
                        comments.append(top_level_comment.body)

                    post_details = {
                        'title': post.title,
                        'url': external_links[0],  # Use the first external link
                        'selftext': post.selftext,
                        'comments': comments,
                        'post_url': f"https://www.reddit.com{post.permalink}",
                        'created_utc': post.created_utc
                    }
                    hottest_posts.append(post_details)
                    if len(hottest_posts) >= limit:
                        break
        print("Fetched posts:", hottest_posts)
        return hottest_posts
    except Exception as e:
        print(f"An error occurred while fetching posts from r/{subreddit_name}: {e}")
        return []

client = openai.OpenAI(api_key=config.OPENAI_API_KEY)

def rewrite_post_for_tweet(post_title, url, selftext, comments, subreddit_name, post_url):
    comments_text = "\n".join(comments[:20])
    prompt = (f"Please take this reddit post and use it to write a twitter thread. The first tweet should just include the exact post title '{post_title}' in double quotes, the external link ({url}) if it exists, otherwise use the {post_url} and relavant hashtags. If an external link ({url}) exists, use that in the first tweet instead of the post url ({post_url}). Always include either the external link OR the post url AND hashtags in the first line / tweet. Always include all of these in the first line. All of this in one line."
              f"Then if there is any text in the post {selftext}, reword it for the titter thread. If the post is in the first person, talk about it as though you're reporting a universal situation. For example if someone says 'I'm looking for a job' your rewording would say somthing like 'people are looking for jobs'"
              f"Finally you should talk about how ETZ, a tax free crypto trading app, can help with investing in a way that's relevant to the content of this post {selftext}. You should talk in first person plural when referring to ETZ usng we or us and not they or them" 
              f"If there is a link in the post to an image or an article please include the link {url} in the post"
              f"Never address me. Just send me the twitter thread"
              f"Never include thread numbers like 1/8 2/8 etc"
              f"Never mention the reddit thread directly in the tweet"
              f"Be factual and never corny of over enthusiastic but feel free to use emojis and always include relvant hashtags"
              f"Never speak in the first person"
              f"Don't make up any facts"
              f"Make sure every tweet makes sense"
              f"Never add any additionsl text that wouldn't go into the tweet and be posted"
              f"Never use sperators of any kind for example --- to destinguish between different tweets in the thread. Just begin the next tweet in the thread on the next line"
              f"Never us links to the ETZ website or app in the twitter thread.")
    
    try:
        print("Sending prompt to OpenAI:", prompt)
        completion = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        tweet = completion.choices[0].message.content.strip()  # Correct method to access the content

        # Log the prompt and tweet response from OpenAI
        print("OpenAI Response:", tweet)

        return tweet
    except Exception as e:
        print(f"An error occurred while processing the prompt: {e}")
        return "Error generating tweet"

if __name__ == "__main__":
    posts = get_hottest_posts('retirement', 1)
    for post in posts:
        print("Reddit Post:", post)
        tweet = rewrite_post_for_tweet(post['title'], post['url'], post['selftext'], post['comments'], 'retirement', post['post_url'])
        print("Tweet:", tweet)
