"""Endpoints for handling user data."""
from flask import Blueprint, jsonify, request
from app.commom.enums.http_verb import HttpVerbENUM
from .service import DisciplineTypeService
from .dto import DisciplineTypeDTO

blueprint: Blueprint = Blueprint("discipline_type", __name__, url_prefix="/api/discipline-types")
discipline_type_dto: DisciplineTypeDTO = DisciplineTypeDTO()

@blueprint.route('/', methods=[HttpVerbENUM.GET.value])
def get_discipline_types(service: DisciplineTypeService):
    """Enpoint - Get discipline_types. """
    return jsonify([discipline_type_dto.dump(discipline_type) for discipline_type in service.get_all()])

@blueprint.route('/<int:discipline_type_id>', methods=[HttpVerbENUM.GET.value])
def get_discipline_type_by_id(service: DisciplineTypeService, discipline_type_id: int):
    """Enpoint - Get discipline_type by id. """
    return jsonify(discipline_type_dto.dump(service.get_by_id(discipline_type_id)))