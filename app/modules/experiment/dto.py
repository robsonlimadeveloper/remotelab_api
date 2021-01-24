'''Experiment dto module'''
from marshmallow import Schema, fields

class ExperimentDTO(Schema):
    '''Experiment dto'''

    id: int = fields.Integer()
    title: str = fields.String()
    description: str = fields.String()
    url_socket_server: str = fields.String()
    url_stream_server: str = fields.String()
    is_active: bool = fields.Boolean()