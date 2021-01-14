"""Exceptions to user data"""
from http import HTTPStatus
from app.core.exceptions_abstract import ErrorAbstract

class UserNotExistWithUsernameAndPasswordException(ErrorAbstract):
    """Exception to credentials not existing"""
    status_code: int = HTTPStatus.UNAUTHORIZED
    message: str = "Username or password is incorrect."