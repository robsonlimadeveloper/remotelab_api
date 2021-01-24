"""User feature model module"""
from app import db

class UserFeature(db.Model):
    """User feature model"""
    __tablename__ = 'user_features'

    id_user_fk: int = db.Column(db.Integer, db.ForeignKey(
        'users.id'), primary_key=True, nullable=False)
    id_feature_fk: int = db.Column(db.Integer, db.ForeignKey(
        'features.id'), primary_key=True, nullable=False)

    def __init__(self, **kwargs):
        super(UserFeature, self).__init__(**kwargs)