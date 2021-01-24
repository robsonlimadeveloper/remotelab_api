"""This module refer Experiment"""
from app import db

class Experiment(db.Model):
    """This class refer Experiments Model"""
    __tablename__ = 'experiments'

    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title: str = db.Column(db.String(255), nullable=False)
    description: str = db.Column(db.String(255), nullable=False)
    url_socket_server: str = db.Column(db.String(255), nullable=False)
    url_stream_server: str = db.Column(db.String(255), nullable=False)
    is_active: bool = db.Column(db.Boolean, default=True, unique=False, nullable=False)

    def __init__(self, **kwargs):
        super(Experiment, self).__init__(**kwargs)