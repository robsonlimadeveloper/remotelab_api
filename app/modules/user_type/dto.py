'''User Type dto module'''
from marshmallow import Schema, fields, validate

class UserTypeDTO(Schema):
    '''User dto'''
    id: int = fields.Integer()
    name: str = fields.String()
    is_active: bool = fields.Boolean()

class UserTypePostDTO(Schema):
    '''User Type POST DTO'''
    name: str = fields.String(validate=validate.Length(min=1), required=True, allow_none=False)