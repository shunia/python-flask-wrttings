from flask import Flask, g, request
from flask_wtf.csrf import CsrfProtect
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask('writtings',
    static_folder='../static',
    template_folder='../static/templates')
babel = None
db = SQLAlchemy(app)

def set_config(conf):
    init(conf)
    config_bp(app)

def init(conf):
    global babel, db
    if conf:
        ''' read conf object '''
        app.config.from_object(conf)
        ''' csrf protection for user login '''
        CsrfProtect(app)

def config_bp(app):
    from app.views.bp_editor import bp as editor
    from app.views.bp_index import bp as index
    from app.views.bp_account import bp as account

    app.register_blueprint(index, url_prefix='')
    app.register_blueprint(editor, url_prefix='/editor')
    app.register_blueprint(account, url_prefix='/account')

def run(host, port):
    app.run(host, port)
