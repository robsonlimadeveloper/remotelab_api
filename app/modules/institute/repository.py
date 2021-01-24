"""Repository to manager institute data"""

from injector import inject
from app.core.repository_abstract import RepositoryAbstract
from .model import Institute

class InstituteRepository(RepositoryAbstract):
    """Class to manager institute data"""
    @inject
    def __init__(self):
        super(InstituteRepository, self).__init__(Institute)