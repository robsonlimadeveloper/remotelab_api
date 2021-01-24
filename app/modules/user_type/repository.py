"""Repository to manager user type data"""

from injector import inject
from app.core.repository_abstract import RepositoryAbstract
from .model import UserType

class UserTypeRepository(RepositoryAbstract):
    """Class to manager user type data"""
    @inject
    def __init__(self):
        super(UserTypeRepository, self).__init__(UserType)
