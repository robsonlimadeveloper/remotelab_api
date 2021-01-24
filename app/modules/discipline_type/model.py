"""This module refer Discipline Type"""
from app import db

class DisciplineType(db.Model):
    """This class refer Discipline Type"""
    __tablename__ = 'discipline_types'

    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name: str = db.Column(db.String(255), nullable=False)
    is_active: bool = db.Column(db.Boolean, default=True, unique=False, nullable=False)

    def __init__(self, **kwargs):
        super(DisciplineType, self).__init__(**kwargs)