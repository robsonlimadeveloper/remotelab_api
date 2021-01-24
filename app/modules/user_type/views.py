"""Endpoints for handling user data."""
from flask import Blueprint, jsonify, request
from app.commom.enums.http_verb import HttpVerbENUM
from .service import UserTypeService
from .dto import UserTypeDTO, UserTypePostDTO

blueprint: Blueprint = Blueprint("user_type", __name__, url_prefix="/api/user-types")
user_type_dto: UserTypeDTO = UserTypeDTO()

@blueprint.route('/', methods=[HttpVerbENUM.GET.value])
def get_user_types(service: UserTypeService):
    """Enpoint - Get all user types. """
    return jsonify([user_type_dto.dump(user) for user in service.get_all()])

@blueprint.route('/<int:user_type_id>', methods=[HttpVerbENUM.GET.value])
def get_user_type_by_id(service: UserTypeService, user_type_id: int):
    """Enpoint - Get user_type by id. """
    return jsonify(user_type_dto.dump(service.get_by_id(user_type_id)))

@blueprint.route('/', methods=[HttpVerbENUM.POST.value])
def register(service: UserTypeService):
    """Endpoint - Register a new User Type"""
    user_type_post_dto: UserTypePostDTO = UserTypePostDTO()

    return jsonify(user_type_dto.dump(service.register(\
        user_type_post_dto.load(request.json))))