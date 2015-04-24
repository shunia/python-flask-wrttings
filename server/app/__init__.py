from flask import Flask, g, request
from flask.ext.babel import Babel
from flask.ext.sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CsrfProtect
from .database import DB

app = Flask('writtings', 
    static_folder='../static', 
    template_folder='../static/templates')
''' csrf protection for user login '''
CsrfProtect(app)
''' i18n support '''
babel = Babel(app)
''' init db '''
db = SQLAlchemy(app)

def set_config(conf):
    init(conf)
    config_bp(app)

def init(conf):
    if conf:
        ''' read conf object '''
        app.config.from_object(conf)

def config_bp(app):
    app.register_blueprint(index, url_prefix='')
    app.register_blueprint(edit, url_prefix='/edit')
    app.register_blueprint(profile, url_prefix='/profile')
    app.register_blueprint(login, url_prefix='/login')

def run(host, port):
    app.run(host, port)

from .views.bp_edit import bp as edit
from .views.bp_index import bp as index
from .views.bp_profile import bp as profile
from .views.bp_login import bp as login