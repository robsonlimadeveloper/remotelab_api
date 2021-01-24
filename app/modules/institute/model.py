"""This module refer Institute"""
from app import db

class Institute(db.Model):
    """This class refer Institute Model"""
    __tablename__ = 'institutes'

    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name: str = db.Column(db.String(255), nullable=False)
    description: str = db.Column(db.String(255), nullable=False)
    code: str = db.Column(db.String(45), nullable=False)
    email: str = db.Column(db.String(255), nullable=False)
    phone: str = db.Column(db.String(45), nullable=False)
    total_hours: int = db.Column(db.Integer)
    is_active: int = db.Column(db.Integer)

    def __init__(self, **kwargs):
        super(Institute, self).__init__(**kwargs)