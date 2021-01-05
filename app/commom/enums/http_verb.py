'''Http Enum module'''

from enum import Enum

class HttpVerbENUM(Enum):
    '''Http Enum'''
    POST = 'POST'
    PUT = 'PUT'
    DELETE = 'DELETE'
    GET = 'GET'
    OPTIONS = 'OPTIONS'

    def __str__(self):
        return self.value
