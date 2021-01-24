'''Institute dto module'''
from marshmallow import Schema, fields

class InstituteDTO(Schema):
    '''Institute dto'''

    id: int = fields.Integer()
    name: str = fields.String()
    description: str = fields.String()
    code: str = fields.String()
    email: str = fields.String()
    is_active: bool = fields.Boolean()
    total_hours: int = fields.Integer()