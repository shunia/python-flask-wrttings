from flask.ext.sqlalchemy import SQLAlchemy

def init_db(app):
    return SQLAlchemy(app)