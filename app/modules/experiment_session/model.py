"""This module refer Experiment Session"""
from datetime import datetime
from app import db

class ExperimentSession(db.Model):
    """This class refer User Model"""
    __tablename__ = 'experiment_sessions'

    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title: str = db.Column(db.String(255), nullable=False)
    description: str = db.Column(db.String(255), nullable=False)
    date_time_begin: datetime = db.Column(db.DateTime(), nullable=False)
    date_time_end: datetime = db.Column(db.DateTime(), nullable=False)
    is_active: bool = db.Column(db.Boolean, default=True, unique=False, nullable=False)
    id_experiment_fk: int = db.Column(db.Integer, db.ForeignKey(
        'experiments.id'), primary_key=True, nullable=False)
    id_user_fk: int = db.Column(db.Integer, db.ForeignKey(
        'users.id'), primary_key=True, nullable=False)
    id_institute_fk: int = db.Column(db.Integer, db.ForeignKey(
        'institutes.id'), primary_key=True, nullable=False)

    def __init__(self, **kwargs):
        super(ExperimentSession, self).__init__(**kwargs)