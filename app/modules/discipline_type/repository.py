"""Repository to manager Discipline Type data"""

from injector import inject
from app.core.repository_abstract import RepositoryAbstract
from .model import DisciplineType

class DisciplineTypeRepository(RepositoryAbstract):
    """Class to manager DisciplineType data"""
    @inject
    def __init__(self):
        super(DisciplineTypeRepository, self).__init__(DisciplineType)