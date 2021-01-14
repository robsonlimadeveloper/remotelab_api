"""
Code for handling user data..
"""

from injector import inject
from app.core.service_abstract import ServiceAbstract
from .repository import UserRepository
from .model import User
from .exceptions import UserNotExistWithUsernameAndPasswordException
from .dto import UserPostDTO

class UserService(ServiceAbstract):
    """
    User service.
    """
    @inject
    def __init__(self, repository: UserRepository):
        super(UserService, self).__init__(repository)
        self.repository = repository
    
    def get_user_by_username_and_password(self, username: str, password: str) -> User:
        """
        GET Users by username and password.
        """
        user: User = self.repository.find_by_username_and_password(username, password)
        print(user.username, user.password)
        if not user:
            raise UserNotExistWithUsernameAndPasswordException

        return user
    
    def register(self, user_post_dto: UserPostDTO)-> User:
        return self.repository.save(User(**user_post_dto, is_active=1, total_hours=10))



