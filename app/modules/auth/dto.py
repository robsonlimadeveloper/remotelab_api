'''Auth dto module'''
from marshmallow import Schema, fields, validate

class AuthDTORequest(Schema):
    '''Auth login dto'''
    username = fields.String(required=True, allow_none=False, validate=validate.Length(min=1))
    password = fields.String(required=True, allow_none=False, validate=validate.Length(min=1))

class AuthDTOResponse(Schema):
    '''Auth token dto'''
    token: str = fields.String()

class AuthUserDTO(Schema):
    '''Auth user dto'''
    id: int = fields.Integer()
    username: str = fields.String()
    password: str = fields.String()