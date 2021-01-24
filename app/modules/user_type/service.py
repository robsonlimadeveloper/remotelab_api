"""
Code for handling user type data..
"""
from injector import inject
from app.core.service_abstract import ServiceAbstract
from .repository import UserTypeRepository
from .model import UserType
from .dto import UserTypePostDTO

class UserTypeService(ServiceAbstract):
    """
    User type service.
    """
    @inject
    def __init__(self, repository: UserTypeRepository):
        super(UserTypeService, self).__init__(repository)
        self.repository = repository
    
    def register(self, user_type_post_dto: UserTypePostDTO)-> UserType:
        return self.repository.save(UserType(**user_type_post_dto, is_active=True))