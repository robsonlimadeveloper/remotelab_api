"""This module refer User"""
from datetime import date
from app import db
from sqlalchemy.dialects.mssql import TINYINT

class User(db.Model):
    """This class refer User Model"""
    __tablename__ = 'users'

    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name: str = db.Column(db.String(255), nullable=False)
    username: str = db.Column(db.String(255), nullable=False)
    password: str = db.Column(db.String(255), nullable=False)
    email: str = db.Column(db.String(255), nullable=False)
    password: str = db.Column(db.String(45), nullable=False)
    phone: str = db.Column(db.String(45), nullable=False)
    date_of_birth: date = db.Column(db.Date(), nullable=True)
    is_active: bool = db.Column(db.Boolean, default=True, unique=False, nullable=False)
    total_hours: int = db.Column(db.Integer)
    id_user_type_fk: int = db.Column(db.Integer, db.ForeignKey('user_types.id'), nullable=True)
    id_user_institute_fk: int = db.Column(db.Integer, db.ForeignKey('institutes.id'), nullable=True)

    features = db.relationship('Feature', secondary='user_features', lazy='subquery',
                               backref=db.backref('users', lazy=True))

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)