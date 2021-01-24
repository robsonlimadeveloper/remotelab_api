"""
Code for handling UserInstitute data..
"""
from injector import inject
from app.core.service_abstract import ServiceAbstract
from .repository import UserInstituteRepository
from .model import UserInstitute

class UserInstituteService(ServiceAbstract):
    """
    UserInstitute service.
    """
    @inject
    def __init__(self, repository: UserInstituteRepository):
        super(UserInstituteService, self).__init__(repository)
        self.repository = repository
