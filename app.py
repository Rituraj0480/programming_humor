from flask import Flask
from hot import hot_blueprint
from new import new_blueprint
from top import top_blueprint

app = Flask(__name__)
app.register_blueprint(hot_blueprint)
app.register_blueprint(new_blueprint)
app.register_blueprint(top_blueprint)