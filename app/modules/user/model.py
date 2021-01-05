"""This module refer User"""

from app import db

class User(db.Model):
    """This class refer User Model"""
    __tablename__ = 'users'

    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name: str = db.Column(db.String(255), nullable=False)
    username: str = db.Column(db.String(255), nullable=False)
    password: str = db.Column(db.String(255), nullable=False)
    email: str = db.Column(db.String(255), nullable=False)

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)