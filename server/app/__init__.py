from flask import Flask
from database import init_db

app = None
db = None

def set_config(config):
    if config:
        app = create_app(config)
        db = create_db(app)

def create_app(config):
    flask = Flask(__name__)
    flask.config.from_object(config)
    return flask

def create_db(app):
    return init_db(app)