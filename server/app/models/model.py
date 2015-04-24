from app import db
from .model_content import content

class User(db.Base):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    
