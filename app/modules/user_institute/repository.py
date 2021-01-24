"""Repository to manager UserInstitute data"""

from injector import inject
from app.core.repository_abstract import RepositoryAbstract
from .model import UserInstitute

class UserInstituteRepository(RepositoryAbstract):
    """Class to manager UserInstitute data"""
    @inject
    def __init__(self):
        super(UserInstituteRepository, self).__init__(UserInstitute)
