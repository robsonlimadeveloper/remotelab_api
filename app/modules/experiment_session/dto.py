'''Experiment Session dto module'''
from marshmallow import Schema, fields, validate
from datetime import datetime

class ExperimentSessionDTO(Schema):
    '''Experiment Session dto'''

    id: int = fields.Integer()
    title: str = fields.String()
    description: str = fields.String()
    date_time_begin: datetime = fields.DateTime()
    date_time_end: datetime = fields.DateTime()
    is_active: bool = fields.Boolean()
    id_user_fk: int = fields.Integer()
    id_institute_fk: int = fields.Integer()

class ExperimentSessionPostDTO(Schema):
    '''Experiment Session Post dto'''

    title: str = fields.String(validate=validate.Length(min=1), required=True, allow_none=False)
    description: str = fields.String(validate=validate.Length(min=1), required=True)
    date_time_begin: datetime = fields.DateTime(required=True, allow_none=False)
    date_time_end: datetime = fields.DateTime(required=True, allow_none=False)
    id_user_fk: int = fields.Integer(required=True, allow_none=False)
    id_institute_fk: int = fields.Integer(required=True, allow_none=False)
    id_experiment_fk: int = fields.Integer(required=True, allow_none=False)