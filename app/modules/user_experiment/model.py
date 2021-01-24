"""UserExperiment model module"""
from app import db

class UserExperiment(db.Model):
    """User Experiment model"""
    __tablename__ = 'user_experiment'

    id_user_fk: int = db.Column(db.Integer, db.ForeignKey(
        'users.id'), primary_key=True, nullable=False)
    id_experiment_fk: int = db.Column(db.Integer, db.ForeignKey(
        'experiments.id'), primary_key=True, nullable=False)

    def __init__(self, **kwargs):
        super(UserExperiment, self).__init__(**kwargs)
