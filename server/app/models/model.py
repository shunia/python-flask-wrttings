from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = 'writtings_user'

    ROLE_GUEST = 0
    ROLE_REGISTERD = 1
    ROLE_VIP = 2
    ROLE_ADMIN = 100

    ''' basic values '''
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    nickname = db.Column(db.String(40), unique=True)
    passhash = db.Column(db.String(40))
    salt = db.Column(db.String(16))
    ''' profile values '''
    name = db.Column(db.String(40))
    age = db.Column(db.Integer)
    sex = db.Column(db.Boolean)
    mobile = db.Column(db.String(20))  # to fit '+' or '()'
    ''' relations '''
    contents = db.Column(db.Text)
    ''' other '''
    role = db.Column(db.Integer)

    def __init__(self, nickname, email, password, role):
        self.nickname = nickname
        self.email = email
        self.set_password(password)
        self.role = role
        self.sex = True
        self.age = 18

    def set_password(self, password):
        if password is not None:
            self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.passhash, password)

import datetime

class content(db.Model):
    __tablename__ = "writtings_user_content"

    id = db.Column(db.Integer, primary_key=True)

    authorid = db.Column(db.Integer, unique=True)
    createdtime = db.Column(db.Integer)
    lastmodifiedtime = db.Column(db.Integer)
    currentversion = db.Column(db.Integer)

    def __init__(self, authorid):
        self.authorid = authorid

class chapter(db.Model):
    __tablename__ = "writtings_chapter"

    id = db.Column(db.Integer, primary_key=True)
    allversions = db.Column(db.Text)
    creationtime = db.Column(db.DateTime)
    lastmodifiedtime = db.Column(db.DateTime)

    def __init__(self, chapid):
        self.creationtime = datetime.datetime.utcnow()
        self.lastmodifiedtime = datetime.datetime.utcnow()

    def add_version(self, version):
        self.allversions = self.allversions

class chapter_content(db.Model):
    __tablename__ = "writtings_chapter_content"

    id = db.Column(db.Integer, primary_key=True)
    cid = db.Column(db.Integer)
    content = db.Column(db.Text)
    version = db.Column(db.Integer)

    def __init__(self, cid, content, version):
        self.cid = cid
        self.content = content
        self.version = version
