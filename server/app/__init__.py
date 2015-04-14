from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from .views.bp_edit import bp as edit
from .views.bp_index import bp as index
from .views.bp_profile import bp as profile
from .views.bp_login import bp as login

app = Flask('writtings', 
    static_folder='../static', 
    template_folder='../static/templates')
db = SQLAlchemy()

def set_config(conf):
    init(conf)
    config_bp(app)

def init(conf):
    if conf:
        app.config.from_object(conf)
        db.init_app(app)

def config_bp(app):
    app.register_blueprint(index, url_prefix='')
    app.register_blueprint(edit, url_prefix='/edit')
    app.register_blueprint(profile, url_prefix='/profile')
    app.register_blueprint(login, url_prefix='/login')