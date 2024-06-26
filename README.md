# Reddit-to-Twitter Automation

This project automates the process of fetching the hottest Reddit posts from specific subreddits and posting them as Twitter threads. It runs on a schedule to post three times per day, ensuring only new and relevant posts are tweeted.

## Prerequisites

1. **Python 3.x**: Ensure you have Python 3 installed.
2. **Virtual Environment**: It's recommended to use a virtual environment to manage dependencies.
3. **Reddit API Credentials**: Register an application on [Reddit](https://www.reddit.com/prefs/apps) to get your client ID, client secret, and user agent.
4. **OpenAI API Key**: Get your API key from [OpenAI](https://beta.openai.com/signup/).
5. **Ayrshare Account**: Create an account on [Ayrshare](https://www.ayrshare.com/) and get your API key for posting to Twitter.
6. **Crontab**: For scheduling tasks on Unix-like systems.

## Setup
#### Clone the Repository

```
git clone https://github.com/SGJIII/reddit-to-twitter.git
git clone <repository-url>
cd reddit-to-twitter
```
#### Create and Activate Virtual Environment
```
python3 -m venv venv
source venv/bin/activate
```
#### Install Dependencies
```
pip install -r requirements.txt
```
#### Configure API Keys
Create a file named config.py in the project directory and add your API keys and other configurations:
```
# config.py
REDDIT_CLIENT_ID = 'your_reddit_client_id'
REDDIT_CLIENT_SECRET = 'your_reddit_client_secret'
REDDIT_USER_AGENT = 'your_reddit_user_agent'
OPENAI_API_KEY = 'your_openai_api_key'
AYRSHARE_API_KEY = 'your_ayrshare_api_key'
```
# Structure
The project structure should look like this:
```
reddit-to-twitter/
├── config.py
├── last_posts.json
├── main.py
├── requirements.txt
├── subreddit_index.json
├── reddit_scraper/
│   └── reddit_scraper.py
└── tweet_scheduler/
    └── tweet_scheduler.py
```
# Usage
#### Running the Script Manually
To run the script manually, use the following command:
```
python main.py
```
#### Setting Up the Scheduler
To automate the script execution using cron:
Open the crontab editor:
```
crontab -e
```
Add the following lines to schedule the script:
```
# Reddit-to-Twitter Automation Schedule (Pacific Time)

# Monday
0 4 * * 1 /path/to/your/venv/bin/python /path/to/your/reddit-to-twitter/main.py
0 11 * * 1 /path/to/your/venv/bin/python /path/to/your/reddit-to-twitter/main.py
0 16 * * 1 /path/to/your/venv/bin/python /path/to/your/reddit-to-twitter/main.py

# Tuesday
0 9 * * 2 /path/to/your/venv/bin/python /path/to/your/reddit-to-twitter/main.py
0 11 * * 2 /path/to/your/venv/bin/python /path/to/your/reddit-to-twitter/main.py
0 16 * * 2 /path/to/your/venv/bin/python /path/to/your/reddit-to-twitter/main.py

# Wednesday
0 12 * * 3 /path/to/your/venv/bin/python /path/to/your/reddit-to-twitter/main.py
0 15 * * 3 /path/to/your/venv/bin/python /path/to/your/reddit-to-twitter/main.py
0 16 * * 3 /path/to/your/venv/bin/python /path/to/your/reddit-to-twitter/main.py

# Thursday
0 0 * * 4 /path/to/your/venv/bin/python /path/to/your/reddit-to-twitter/main.py
0 10 * * 4 /path/to/your/venv/bin/python /path/to/your/reddit-to-twitter/main.py
0 11 * * 4 /path/to/your/venv/bin/python /path/to/your/reddit-to-twitter/main.py

# Friday
0 0 * * 5 /path/to/your/venv/bin/python /path/to/your/reddit-to-twitter/main.py
0 11 * * 5 /path/to/your/venv/bin/python /path/to/your/reddit-to-twitter/main.py
0 13 * * 5 /path/to/your/venv/bin/python /path/to/your/reddit-to-twitter/main.py

# Saturday
0 20 * * 6 /path/to/your/venv/bin/python /path/to/your/reddit-to-twitter/main.py
0 21 * * 6 /path/to/your/venv/bin/python /path/to/your/reddit-to-twitter/main.py
0 22 * * 6 /path/to/your/venv/bin/python /path/to/your/reddit-to-twitter/main.py

# Sunday
0 0 * * 7 /path/to/your/venv/bin/python /path/to/your/reddit-to-twitter/main.py
0 15 * * 7 /path/to/your/venv/bin/python /path/to/your/reddit-to-twitter/main.py
0 19 * * 7 /path/to/your/venv/bin/python /path/to/your/reddit-to-twitter/main.py

```
Save and exit the crontab editor.
### Notes
Ensure your Mac is on and awake during the scheduled times.
To keep mac awake you can use cafinate
```
caffeinate -s
```
The terminal does not need to be open for cron jobs to run.
Adjust the schedule as needed to fit your requirements.
### Troubleshooting
If the script is not running as expected, check the cron logs for errors.
Ensure all dependencies are correctly installed in the virtual environment.
Verify that your API keys and configuration are correct.
### License
This project is licensed under the MIT License.