"""Repository to manager Experiment Session data"""

from injector import inject
from app.core.repository_abstract import RepositoryAbstract
from .model import ExperimentSession

class ExperimentSessionRepository(RepositoryAbstract):
    """Class to manager ExperimentSession data"""
    @inject
    def __init__(self):
        super(ExperimentSessionRepository, self).__init__(ExperimentSession)