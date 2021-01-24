"""ExperimentDiscipline model module"""
from app import db

class ExperimentDiscipline(db.Model):
    """ExperimentDiscipline model"""
    __tablename__ = 'experiment_disciplines'

    id_experiment_fk: int = db.Column(db.Integer, db.ForeignKey(
        'experiments.id'), primary_key=True, nullable=False)
    id_discipline_fk: int = db.Column(db.Integer, db.ForeignKey(
        'discipline_types.id'), primary_key=True, nullable=False)

    def __init__(self, **kwargs):
        super(ExperimentDiscipline, self).__init__(**kwargs)