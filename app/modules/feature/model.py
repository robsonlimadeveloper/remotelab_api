"""This module refer Feature"""
from app import db

class Feature(db.Model):
    """This class refer Feature Model"""
    __tablename__ = 'features'

    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name: str = db.Column(db.String(255), nullable=False)
    is_active: bool = db.Column(db.Boolean, default=True, unique=False, nullable=False)

    def __init__(self, **kwargs):
        super(Feature, self).__init__(**kwargs)