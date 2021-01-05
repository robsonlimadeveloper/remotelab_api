'''Handler error module'''
from http import HTTPStatus
from marshmallow import ValidationError
from flask import jsonify, make_response
from werkzeug.exceptions import HTTPException
from app import app
from .exceptions_abstract import ErrorAbstract

@app.errorhandler(ErrorAbstract)
def handle_exception_name_duplicate(exception: ErrorAbstract):
    '''Handler name duplicate'''
    return make_response(jsonify({'error': exception.message}), exception.status_code)

@app.errorhandler(ValidationError)
def handle_exception_bad_request(exception: ValidationError):
    '''Handler bad request'''
    return make_response(jsonify({'error': exception.messages}), HTTPStatus.BAD_REQUEST)

@app.errorhandler(Exception)
def handle_error(error):
    """ Api Handle error """
    code = 500
    if isinstance(error, HTTPException):
        code = error.code
    return jsonify(error=str(error)), code
