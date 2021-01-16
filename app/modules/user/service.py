"""
Code for handling user data..
"""
from injector import inject
from app.core.service_abstract import ServiceAbstract
from .repository import UserRepository
from .model import User
from .exceptions import UserNotExistWithUsernameAndPasswordException,\
    UserWithUsernameExistsException, UserNotFoundException
from .dto import UserPostDTO, UserUpdateDTO

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
        
        if not user:
            raise UserNotExistWithUsernameAndPasswordException

        return user

    def __verify_username_exists(self, username: str)-> User:
        """Checks if there are any users with the same username."""
        user: User = self.repository.find_by_username(username)

        if user:
            raise UserWithUsernameExistsException

        return user
    
    def __validate_username_to_update(self, username: str, user_to_update: User):
        """Validate is update username is valid"""
        user: User = self.repository.find_by_username(username)

        if user and user.id != user_to_update.id:
            raise UserWithUsernameExistsException

    def register(self, user_post_dto: UserPostDTO)-> User:
        """Register a new User"""
        self.__verify_username_exists(user_post_dto["username"])

        return self.repository.save(User(**user_post_dto, is_active=1, total_hours=10))
    
    def update(self, user_update_dto: UserUpdateDTO, user_id: int) -> User:
        """Update a User"""
        user: User = self.get_by_id(user_id)
        self.__validate_username_to_update(user_update_dto["username"], user)

        return self.repository.update(user_id, User(**user_update_dto,\
             total_hours=user.total_hours, is_active=user.is_active))

    def get_by_id(self, user_id: int) -> User:
        """Return User by Id"""
        user: User = self.repository.find_by_id(user_id)

        if not user:
            raise UserNotFoundException

        return user
        