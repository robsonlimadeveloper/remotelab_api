"""Endpoints for handling user data."""
from flask import Blueprint, jsonify, request
from app.commom.enums.http_verb import HttpVerbENUM
from .service import ExperimentSessionService
from .dto import ExperimentSessionDTO, ExperimentSessionPostDTO

blueprint: Blueprint = Blueprint("experiment_session", __name__, url_prefix="/api/experiment-sessions")
experiment_session_dto: ExperimentSessionDTO = ExperimentSessionDTO()

@blueprint.route('/', methods=[HttpVerbENUM.GET.value])
def get_experiment_sessions(service: ExperimentSessionService):
    """Enpoint - Get all experiment sessions. """
    return jsonify([experiment_session_dto.dump(experiment_session) for experiment_session in service.get_all()])

@blueprint.route('/<int:experiment_session_id>', methods=[HttpVerbENUM.GET.value])
def get_experiment_session_by_id(service: ExperimentSessionService, experiment_session_id: int):
    """Enpoint - Get experiment session by id. """
    return jsonify(experiment_session_dto.dump(service.get_by_id(experiment_session_id)))

@blueprint.route('/', methods=[HttpVerbENUM.POST.value])
def register(service: ExperimentSessionService):
    """Enpoint - Register a new experiment session. """
    experiment_session_post_dto: ExperimentSessionPostDTO = ExperimentSessionPostDTO()

    return jsonify(experiment_session_dto.dump(service.register(\
        experiment_session_post_dto.load(request.json))))

@blueprint.route('/<int:experiment_session_id>', methods=[HttpVerbENUM.DELETE.value])
def delete_experiment_session_by_id(service: ExperimentSessionService, experiment_session_id: int):
    """Enpoint - Delete experiment session by id. """
    return jsonify(experiment_session_dto.dump(service.remove(experiment_session_id)))