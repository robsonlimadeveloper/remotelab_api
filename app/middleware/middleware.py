'''Middleware module'''
from http import HTTPStatus
import os
import jwt
from typing import List
from flask import Flask, Request, Response
from app.commom.enums.http_verb import HttpVerbENUM

class Middleware:
    '''Middleware class'''
    # pylint: disable=too-few-public-methods
    ALLOWED_TOKEN_SIZE: int = 2
    ALLOWED_SCHEME: str = 'Bearer'

    def __init__(self, app: Flask):
        self.app = app

    def __call__(self, environ: dict, start_response):
        #return self.app(environ, start_response) #No authentication

        request: Request = Request(environ)
        
        if request.path == "/api/auth/" \
            or request.method == HttpVerbENUM.OPTIONS.value:
            return self.app(environ, start_response)

        res: Response = Response(mimetype='text/json', status=HTTPStatus.UNAUTHORIZED)
        authorization: str = request.headers.get('Authorization')

        if authorization and authorization is not None:
            auth_list: List[str] = authorization.split(' ')

            if (not len(auth_list) == self.ALLOWED_TOKEN_SIZE) \
                or (auth_list[0] != self.ALLOWED_SCHEME):
                res.response = "Bad Authorization header. Expected value 'Bearer JWT'"

                return res(environ, start_response)

            try:
                token = jwt.decode(auth_list[1], os.environ["SECRET_KEY"])
                user: dict = token["user"]
                environ['user_id']: int = user['id']
                return self.app(environ, start_response)

            except jwt.ExpiredSignatureError:
                res.response = "Expired authorization"

                return res(environ, start_response)

            except jwt.exceptions.DecodeError:
                res.response = "Token with invalid format"
                return res(environ, start_response)

        else:
            res.response = "Authorization header not found"

            return res(environ, start_response)
      
