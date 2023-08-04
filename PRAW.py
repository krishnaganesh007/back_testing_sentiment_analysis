# import pandas as pd
# check_df = pd.read_csv("./dating_data.csv")


import requests
import requests.auth
client_auth = requests.auth.HTTPBasicAuth('CmdiukiJLVJ3XuqG6jp9kQ', 'zuLe30DkKPPfL1JA6yYaaLpvH8Y9Lw')
post_data = {"grant_type": "password", "username": "reddit_bot", "password": "snoo"}
headers = {"User-Agent": "ChangeMeClient/0.1 by krishgan007"}
response = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data, headers=headers)
response.json()


import praw
reddit = praw.Reddit(client_id='', client_secret='', user_agent='krishnaScrapes')


hot_posts = reddit.subreddit('MachineLearning').hot(limit=10)
for post in hot_posts:
    print(post.title)

hot_posts = reddit.subreddit('all').hot(limit=10)
for post in hot_posts:
    print(post.title)

submission = reddit.submission(id="a3p0uq")
from praw.models import MoreComments
for top_level_comment in submission.comments:
    if isinstance(top_level_comment, MoreComments):
        continue
    print(top_level_comment.body)