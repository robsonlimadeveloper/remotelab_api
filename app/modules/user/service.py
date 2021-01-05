"""
Code for handling user data..
"""

from injector import inject
from app.core.service_abstract import ServiceAbstract
from .repository import UserRepository
from .model import User

class UserService(ServiceAbstract):
    """
    User service.
    """
    @inject
    def __init__(self, repository: UserRepository):
        super(UserService, self).__init__(repository)
        self.repository = repository
