"""Repository to manager Experiment data"""

from injector import inject
from app.core.repository_abstract import RepositoryAbstract
from .model import Experiment

class ExperimentRepository(RepositoryAbstract):
    """Class to manager Experiment data"""
    @inject
    def __init__(self):
        super(ExperimentRepository, self).__init__(Experiment)