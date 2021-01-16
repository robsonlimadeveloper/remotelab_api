"""Exceptions to user data"""
from http import HTTPStatus
from app.core.exceptions_abstract import ErrorAbstract

class UserNotExistWithUsernameAndPasswordException(ErrorAbstract):
    """Exception to credentials not existing"""
    status_code: int = HTTPStatus.UNAUTHORIZED
    message: str = "Username or password is incorrect."

class UserWithUsernameExistsException(ErrorAbstract):
    """Username exists in database"""
    status_code: int = HTTPStatus.NOT_ACCEPTABLE
    message: str = "Username already exists in our database.."