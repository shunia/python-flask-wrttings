from flask import g

class DB(object):
    from flask.ext.sqlalchemy import SQLAlchemy
    
    def __init__(self, app=None):
        self.db = SQLAlchemy(app)

def connect_db():
    return None

def conn_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = connect_db()
    return db

def close_db(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()