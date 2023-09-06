# import pandas as pd
# check_df = pd.read_csv("./dating_data.csv")


import requests
import requests.auth
client_auth = requests.auth.HTTPBasicAuth('CmdiukiJLVJ3XuqG6jp9kQ', 'zuLe30DkKPPfL1JA6yYaaLpvH8Y9Lw')
post_data = {"grant_type": "password", "username": "reddit_bot", "password": "snoo"}
headers = {"User-Agent": "ChangeMeClient/0.1 by krishgan007"}
response = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data, headers=headers)
response.json()


import pandas as pd

import praw
reddit = praw.Reddit(client_id='', client_secret='', user_agent='krishnaScrapes')


hot_posts = reddit.subreddit('elonmusk').hot(limit=100)

reddit_df = pd.DataFrame()
for post in hot_posts:

    comment_list = []
    for comment in post.comments:
        #print(comment.body)
        comment_list.append(comment.body)
    
    tmp_df = pd.DataFrame()
    tmp_df["comments_list"] = comment_list
    tmp_df["post_id"] = post.id
    tmp_df["post_title"] = post.title
    

    reddit_df = pd.concat([reddit_df, tmp_df], axis = 0 )

reddit_df = reddit_df.reset_index(drop = True)
reddit_df.to_csv("./reddit_tesla_posts_comments_top100.csv", index = False)

hot_posts = reddit.subreddit('all').hot(limit=10)
for post in hot_posts:
    print(post.title)

submission = reddit.submission(id="a3p0uq")
from praw.models import MoreComments
for top_level_comment in submission.comments:
    if isinstance(top_level_comment, MoreComments):
        continue
    print(top_level_comment.body)