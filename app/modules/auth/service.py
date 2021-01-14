'''Auth service module'''
import os
import datetime
import json
from typing import Mapping
from http import HTTPStatus
import jwt
from injector import inject
import requests
from flask import Response
from app.modules.user.model import User
from app.modules.user.service import UserService
from app.modules.user.dto import UserDTO
from .dto import AuthDTORequest, AuthDTOResponse, AuthUserDTO

auth_user_dto: AuthUserDTO = AuthUserDTO()
auth_dto_response: AuthDTOResponse = AuthDTOResponse()

class AuthService:
    '''Auth service class'''

    @inject
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def token_encode(self, credencials: dict) -> str:
        '''token_encode method'''
        user: User = self.user_service.get_user_by_username_and_password(\
            credencials["username"], credencials["password"])

        token: str = jwt.encode(
            {
                'user': auth_user_dto.dump(user),
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1)
            },
            os.environ["SECRET_KEY"],
            algorithm='HS256'
        )

        return token

    def authenticate(self, credentials: AuthDTORequest) -> dict:
        '''authenticate method'''
        token: str = self.token_encode(credentials)

        return auth_dto_response.dump(dict(token=token))
