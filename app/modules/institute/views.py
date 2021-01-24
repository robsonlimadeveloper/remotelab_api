"""Endpoints for handling user data."""
from flask import Blueprint, jsonify, request
from app.commom.enums.http_verb import HttpVerbENUM
from .service import InstituteService
from .dto import InstituteDTO

blueprint: Blueprint = Blueprint("institute", __name__, url_prefix="/api/institutes")
institute_dto: InstituteDTO = InstituteDTO()

@blueprint.route('/', methods=[HttpVerbENUM.GET.value])
def get_institutes(service: InstituteService):
    """Enpoint - Get all institutes. """
    return jsonify([institute_dto.dump(institute) for institute in service.get_all()])

@blueprint.route('/<int:institute_id>', methods=[HttpVerbENUM.GET.value])
def get_institute_by_id(service: InstituteService, institute_id: int):
    """Enpoint - Get institutes by id. """
    return jsonify(institute_dto.dump(service.get_by_id(institute_id)))