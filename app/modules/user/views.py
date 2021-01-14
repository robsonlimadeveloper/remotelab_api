"""Endpoints for handling user data."""
from flask import Blueprint, jsonify, request
from app.commom.enums.http_verb import HttpVerbENUM
from .service import UserService
from .dto import UserDTO, UserPostDTO

blueprint: Blueprint = Blueprint("user", __name__, url_prefix="/api/users")
user_dto = UserDTO()

@blueprint.route('/', methods=[HttpVerbENUM.GET.value])
def get_users(service: UserService):
    """Enpoint - Get all users. """
    return jsonify([user_dto.dump(user) for user in service.get_all()])

@blueprint.route('/<int:user_id>', methods=[HttpVerbENUM.GET.value])
def get_user_by_id(service: UserService, user_id: int):
    """Enpoint - Get user by id. """
    return jsonify(user_dto.dump(service.get_by_id(user_id)))

@blueprint.route('/', methods=[HttpVerbENUM.POST.value])
def register(service: UserService):
    """Endpoint - Register a new User"""
    user_post_dto: UserPostDTO = UserPostDTO()

    return jsonify(user_dto.dump(service.register(user_post_dto.load(request.json))))
