'''User Substitute dto module'''
from marshmallow import Schema, fields

class UserDTO(Schema):
    '''User dto'''
    id: int = fields.Integer()
    name: str = fields.String()
    username: str = fields.String()
    email: str = fields.String()