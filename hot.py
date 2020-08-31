from flask import Blueprint
from flask import Flask, render_template
import praw

hot_blueprint = Blueprint('hot_blueprint', __name__)

@hot_blueprint.route('/')
def get_post():
    f = open("key.txt", "r")
    key = f.read().split(',')
    reddit = praw.Reddit(client_id=key[0],
                     client_secret=key[1],
                        user_agent = key[2])

    sub_reddit = reddit.subreddit("ProgrammerHumor")
    res = []
    for submission in sub_reddit.hot(limit=20):
        title = submission.title
        url = submission.url
        res.append([title, url])
    
    return render_template("hot.html", res = res)
