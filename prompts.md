prompt = f"Rewrite the following post into a tweet and include the link: {post_title} {selftext} {url}. Make sure to include the link {url} in your response"

prompt = f"Please read the following content: {post_title} {comments_text} {sefltext}. Then rewrite it into a tweet and be 100% sure to include the link {url}"

f"Also say something about how ETZ helps with tax free traiding and retirement")


    prompt = (
              f"Please take the context from this reddit post and use it to write a twitter thread promoting ETZ, a tax advantage crypto app where you can buy sell and trade crypto without paying capital gains tax: {post_title} {selftext} {comments}. "
              f"Be sure to focus more on using the context of the reddit post, almost like you're reportind a story than promoting etz but you can slide it in when it makes sense"
              f"If there is a link in the post to an image or an article please include the link {url} in the post"
              f"Never address me. Just send me the twitter thread"
              f"Never include thread numbers like 1/8 2/8 etc"
              f"Never mention the reddit thread directly in the tweet"
              f"Be factual and never corny of over enthusiastic but feel free to use emojis and always include relvant hashtags"
              f"Never speak in the first person"
              f"Don't make up any facts"
              f"Make sure every twee makes sense"
              f"Never add any additionsl text that wouldn't go in the tweet and be posted"
              f"Here are the links to the website: https://etzsoft.com/ and the app:https://etz.app.link/I3UYLNkUvKb"



    prompt = (f"Please take this reddit post and use it to write a twitter thread. The first tweet should just include the exact post title '{post_title}' in double quotes, the link to the post {post_url} and relavant hashtags."
              f"Then if there is any text in the post {selftext}, reword it for the titter thread."
              f"Finally you should talk about how ETZ, a tax advantage crypto app where you can buy sell and trade crypto instantly in retirement accounts without paying capital gains tax, can help with {subreddit_name} investing." 
              f"If there is a link in the post to an image or an article please include the link {url} in the post"
              f"Never address me. Just send me the twitter thread"
              f"Never include thread numbers like 1/8 2/8 etc"
              f"Never mention the reddit thread directly in the tweet"
              f"Be factual and never corny of over enthusiastic but feel free to use emojis and always include relvant hashtags"
              f"Never speak in the first person"
              f"Don't make up any facts"
              f"Make sure every tweet makes sense"
              f"Never add any additionsl text that wouldn't go into the tweet and be posted"
              f"Here are the links to the website: https://etzsoft.com/ and the app:https://etz.app.link/I3UYLNkUvKb")


Creates a Tweet on behalf of an authenticated user.

New in version 4.3.

Changed in version 4.5: Added user_auth parameter

Parameters
direct_message_deep_link (str | None) – Tweets a link directly to a Direct Message conversation with an account.

for_super_followers_only (bool | None) – Allows you to Tweet exclusively for Super Followers.

place_id (str | None) – Place ID being attached to the Tweet for geo location.

media_ids (list[int | str] | None) – A list of Media IDs being attached to the Tweet. This is only required if the request includes the tagged_user_ids.

media_tagged_user_ids (list[int | str] | None) – A list of User IDs being tagged in the Tweet with Media. If the user you’re tagging doesn’t have photo-tagging enabled, their names won’t show up in the list of tagged users even though the Tweet is successfully created.

poll_duration_minutes (int | None) – Duration of the poll in minutes for a Tweet with a poll. This is only required if the request includes poll.options.

poll_options (list[str] | None) – A list of poll options for a Tweet with a poll.

quote_tweet_id (int | str | None) – Link to the Tweet being quoted.

exclude_reply_user_ids (list[int | str] | None) – A list of User IDs to be excluded from the reply Tweet thus removing a user from a thread.

in_reply_to_tweet_id (int | str | None) – Tweet ID of the Tweet being replied to. Please note that in_reply_to_tweet_id needs to be in the request if exclude_reply_user_ids is present.

reply_settings (str | None) – Settings to indicate who can reply to the Tweet. Limited to “mentionedUsers” and “following”. If the field isn’t specified, it will default to everyone.

text (str | None) – Text of the Tweet being created. This field is required if media.media_ids is not present.

user_auth (bool) – Whether or not to use OAuth 1.0a User Context to authenticate

Introduction
Tweepy supports the OAuth 1.0a User Context, OAuth 2.0 Bearer Token (App-Only), and OAuth 2.0 Authorization Code Flow with PKCE (User Context) authentication methods.

Twitter API v1.1
OAuth 2.0 Bearer Token (App-Only)
The simplest way to generate a bearer token is through your app’s Keys and Tokens tab under the Twitter Developer Portal Projects & Apps page.

You can then initialize OAuth2BearerHandler with the bearer token and initialize API with the OAuth2BearerHandler instance:

import tweepy

auth = tweepy.OAuth2BearerHandler("Bearer Token here")
api = tweepy.API(auth)
Alternatively, you can use the API / Consumer key and secret that can be found on the same page and initialize OAuth2AppHandler instead:

import tweepy

auth = tweepy.OAuth2AppHandler(
"API / Consumer Key here", "API / Consumer Secret here"
)
api = tweepy.API(auth)
OAuth 1.0a User Context
Similarly, the simplest way to authenticate as your developer account is to generate an access token and access token secret through your app’s Keys and Tokens tab under the Twitter Developer Portal Projects & Apps page.

You’ll also need the app’s API / consumer key and secret that can be found on that page.

You can then initialize OAuth1UserHandler with all four credentials and initialize API with the OAuth1UserHandler instance:

import tweepy

auth = tweepy.OAuth1UserHandler(
"API / Consumer Key here", "API / Consumer Secret here",
"Access Token here", "Access Token Secret here"
)
api = tweepy.API(auth)
To authenticate as a different user, see 3-legged OAuth.

Twitter API v2
Tweepy’s interface for Twitter API v2, Client, handles OAuth 2.0 Bearer Token (application-only) and OAuth 1.0a User Context authentication for you.

OAuth 2.0 Bearer Token (App-Only)
The simplest way to generate a bearer token is through your app’s Keys and Tokens tab under the Twitter Developer Portal Projects & Apps page.

You can then simply pass the bearer token to Client when initializing it:

import tweepy

client = tweepy.Client("Bearer Token here")
OAuth 1.0a User Context
Similarly, the simplest way to authenticate as your developer account is to generate an access token and access token secret through your app’s Keys and Tokens tab under the Twitter Developer Portal Projects & Apps page.

You’ll also need the app’s API / consumer key and secret that can be found on that page.

You can then simply pass all four credentials to Client when initializing it:

import tweepy

client = tweepy.Client(
consumer_key="API / Consumer Key here",
consumer_secret="API / Consumer Secret here",
access_token="Access Token here",
access_token_secret="Access Token Secret here"
)
To authenticate as a different user, see 3-legged OAuth.

OAuth 2.0 Authorization Code Flow with PKCE (User Context)
You can generate an access token to authenticate as a user using OAuth2UserHandler.

You’ll need to turn on OAuth 2.0 under the User authentication settings section of your app’s Settings tab under the Twitter Developer Portal Projects & Apps page. To do this, you’ll need to provide a Callback / Redirect URI / URL.

Then, you’ll need to note the app’s Client ID, which you can find through your app’s Keys and Tokens tab under the Twitter Developer Portal Projects & Apps page. If you’re using a confidential client, you’ll also need to generate a Client Secret.

You can then initialize OAuth2UserHandler with the scopes you need:

import tweepy

oauth2_user_handler = tweepy.OAuth2UserHandler(
client_id="Client ID here",
redirect_uri="Callback / Redirect URI / URL here",
scope=["Scope here", "Scope here"],
# Client Secret is only necessary if using a confidential client
client_secret="Client Secret here"
)
For a list of scopes, see the Scopes section of Twitter’s OAuth 2.0 Authorization Code Flow with PKCE documentation.

Then, you can get the authorization URL:

print(oauth2_user_handler.get_authorization_url())
This can be used to have a user authenticate your app. Once they’ve done so, they’ll be redirected to the Callback / Redirect URI / URL you provided. You’ll need to pass that authorization response URL to fetch the access token:

access_token = oauth2_user_handler.fetch_token(
"Authorization Response URL here"
)
You can then pass the access token to Client when initializing it:

client = tweepy.Client("Access Token here")

And here's that explanation again:
This issue was solved for me by a Contributor to the Tweepy project, Harmon758, via discussion # 2006 on the Tweepy GitHub.

The solution required two things. First, setting the user_auth parameter to False when calling the .get_me() method. This must be done because the function defaults to OAuth 1.0 if not.

And then second, because after I did this I got a 401 unauthorized error, I needed to tweak the format of the Access Token that I was passing through to the Client object. I was trying to pass through ‘access_token’ in the above code, but it should have been ‘access_token[“access_token”]’. The return from the .fetch_token() method is a dictionary that contains the required field.

Correct code:

Build handler with:

oauth2_user_handler = tweepy.OAuth2UserHandler(
client_id='your_client_id',
redirect_uri="your_redirect_uri",
scope=["tweet.read", "and any others you need"],
# Client Secret is only necessary if using a confidential client
client_secret='your_client_secret'
)
Redirect to Twitter for authorization with:

def auth(request):

kotlin
Copy code
return HttpResponseRedirect(oauth2_user_handler.get_authorization_url())
And finally, callback to:

def callback(request):

scss
Copy code
access_token = oauth2_user_handler.fetch_token(request.build_absolute_uri())

user_client = tweepy.Client(
    access_token["access_token"]
)

me = user_client.get_me(user_auth=False)

return HttpResponse()

