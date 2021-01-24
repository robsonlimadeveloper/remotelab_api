'''Discipline Type dto module'''
from marshmallow import Schema, fields

class DisciplineTypeDTO(Schema):
    '''Discipline Type dto'''

    id: int = fields.Integer()
    name: str = fields.String()
    is_active: bool = fields.Boolean()
    