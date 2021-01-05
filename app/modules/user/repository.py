"""Repository to manager user data"""

from injector import inject
from app.core.repository_abstract import RepositoryAbstract
from .model import User

class UserRepository(RepositoryAbstract):
    """Class to manager user data"""
    @inject
    def __init__(self):
        super(UserRepository, self).__init__(User)