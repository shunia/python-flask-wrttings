from flask import Flask, g, request
from flask_wtf.csrf import CsrfProtect
from .database import init_db

app = Flask('writtings', 
    static_folder='../static', 
    template_folder='../static/templates')
babel = None
db = None

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
        ''' init db '''
        db = init_db(app)

def config_bp(app):
    from .views.bp_edit import bp as edit
    from .views.bp_index import bp as index
    from .views.bp_account import bp as account

    app.register_blueprint(index, url_prefix='')
    app.register_blueprint(edit, url_prefix='/edit')
    app.register_blueprint(account, url_prefix='/account')

def run(host, port):
    app.run(host, port)