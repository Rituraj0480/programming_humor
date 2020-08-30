from flask import Blueprint
from flask import Flask, render_template
import praw

hot_blueprint = Blueprint('hot_blueprint', __name__)

@hot_blueprint.route('/')
def get_post():
    reddit = praw.Reddit(client_id="WpL-adBFuXHpsg",
                     client_secret="JhSLFa8NN4IjZLD0AiVq4X6BUL4",
                        user_agent = "programming_humor 1.0 by /u/rituraj0480")

    sub_reddit = reddit.subreddit("ProgrammerHumor")
    res = []
    for submission in sub_reddit.hot(limit=20):
        title = submission.title
        url = submission.url
        res.append([title, url])
    
    return render_template("hot.html", res = res)
