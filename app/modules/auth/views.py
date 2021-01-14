'''Auth module'''
from flask import Blueprint, request
from .service import AuthService
from .dto import AuthDTORequest

auth_dto_request = AuthDTORequest()
blueprint: Blueprint = Blueprint("auth", __name__, url_prefix="/api/auth")


@blueprint.route("/", methods=["POST"])
def login(service: AuthService):
    '''Login route'''
    data_authenticate: dict = service.authenticate(auth_dto_request.load(request.json))
    return data_authenticate
