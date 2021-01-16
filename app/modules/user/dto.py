'''User Substitute dto module'''
from marshmallow import Schema, fields, validate
from datetime import date

class UserDTO(Schema):
    '''User dto'''
    id: int = fields.Integer()
    name: str = fields.String()
    username: str = fields.String()
    email: str = fields.String()
    phone: str = fields.String()
    date_of_birth: date = fields.Date()
    is_active: bool = fields.Boolean()
    total_hours: int = fields.Integer()

class UserPostDTO(Schema):
    '''User POST DTO'''
    name: str = fields.String(validate=validate.Length(min=1), required=True, allow_none=False)
    username: str = fields.String()
    email: str = fields.String()
    phone: str = fields.String()
    date_of_birth: date = fields.Date()
    password: str = fields.String(validate=validate.Length(min=1), required=True, allow_none=False)

class UserUpdateDTO(Schema):
    '''User Update DTO'''
    name: str = fields.String(validate=validate.Length(min=1), required=True, allow_none=False)
    username: str = fields.String()
    email: str = fields.String()
    phone: str = fields.String()
    date_of_birth: date = fields.Date()
    password: str = fields.String(validate=validate.Length(min=1), required=True, allow_none=False)
    