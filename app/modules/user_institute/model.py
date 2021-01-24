"""UserInstitute model module"""
from app import db

class UserInstitute(db.Model):
    """UserInstitute model"""
    __tablename__ = 'users_institute'

    id_user_fk: int = db.Column(db.Integer, db.ForeignKey(
        'users.id'), primary_key=True, nullable=False)
    id_institute_fk: int = db.Column(db.Integer, db.ForeignKey(
        'institutes.id'), primary_key=True, nullable=False)

    def __init__(self, **kwargs):
        super(UserInstitute, self).__init__(**kwargs)
