'''Experiment dto module'''
from marshmallow import Schema, fields, validate

class ExperimentDTO(Schema):
    '''Experiment dto'''

    id: int = fields.Integer()
    title: str = fields.String()
    description: str = fields.String()
    url_socket_server: str = fields.String()
    url_stream_server: str = fields.String()
    is_active: bool = fields.Boolean()

class ExperimentPostDTO(Schema):
    '''Experiment post dto'''

    title: str = fields.String(validate=validate.Length(min=1), required=True, allow_none=False)
    description: str = fields.String(validate=validate.Length(min=1), required=True, allow_none=False)
    url_socket_server: str = fields.String(required=True, allow_none=False)
    url_stream_server: str = fields.String(required=True, allow_none=False)
