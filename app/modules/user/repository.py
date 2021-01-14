"""Repository to manager user data"""

from injector import inject
from app.core.repository_abstract import RepositoryAbstract
from .model import User

class UserRepository(RepositoryAbstract):
    """Class to manager user data"""
    @inject
    def __init__(self):
        super(UserRepository, self).__init__(User)
    
    def find_by_username_and_password(self, username: str, password: str) -> User:
        """Return user by username and password"""
        return (self.session
                .query(User)
                .filter(User.username == username)
                .filter(User.password == password)
                .first())