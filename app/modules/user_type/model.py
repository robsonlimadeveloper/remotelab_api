"""This module refer User Type"""
from app import db

class UserType(db.Model):
    """This class refer User Type Model"""
    __tablename__ = 'user_types'

    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name: str = db.Column(db.String(255), nullable=False)
    is_active: bool = db.Column(db.Boolean, default=True, unique=False, nullable=False)

    def __init__(self, **kwargs):
        super(UserType, self).__init__(**kwargs)