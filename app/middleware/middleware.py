'''Middleware module'''
from http import HTTPStatus
import os
from typing import List
from flask import Flask, Request, Response
from app.commom.enums.http_verb import HttpVerbENUM

class Middleware:
    '''Middleware class'''

    def __init__(self, app: Flask):
        self.app = app

    def __call__(self, environ: dict, start_response):
        return self.app(environ, start_response)
      
