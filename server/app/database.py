from app import app
from flask import g
from flask.ext.sqlalchemy import SQLAlchemy

def connect_db():

@app.before_request
def conn_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = connect_db()
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()