from unittest import TestCase
from unittest.mock import patch
from typing import List
from injector import Injector
from app.modules.user.service import UserService
from app.modules.user.repository import UserRepository
from app.modules.user.model import User
from . import DependencyModule

class TestUser(TestCase):
    """Class from user service"""

    def setUp(self):
        self.injector = Injector(DependencyModule(UserService, UserRepository))
    
    @classmethod
    def __prepare_data_user(cls) -> dict:
        user_data: dict = {
            "username":  "admin",
            "name":  "Admin",
            "password":  "1234",
            "email": "admin@admin.com",
            "phone": "+55 83 9999-9999",
            "date_of_birth": "1990-07-04"
        }
        return user_data

    @patch("app.modules.user.service.UserRepository.save")
    @patch("app.modules.user.repository.UserRepository.find_by_username")
    def test_user_register_verify_if_not_exists(self, mock_find, mock_save):
        """ Test user register verify if username not exists"""

        user = User(
            username="admin"
        )

        mock_find.return_value = None
        mock_save.return_value = user

        resp: User = self.injector.get(
            UserService).register(self.__prepare_data_user())

        self.assertEqual(resp.username, "admin")
        self.assertIsInstance(resp, User)