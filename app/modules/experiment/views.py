"""Endpoints for handling Experiment data."""
from flask import Blueprint, jsonify, request
from app.commom.enums.http_verb import HttpVerbENUM
from .service import ExperimentService
from .dto import ExperimentDTO

blueprint: Blueprint = Blueprint("experiment", __name__, url_prefix="/api/experiments")
experiment_dto: ExperimentDTO = ExperimentDTO()

@blueprint.route('/', methods=[HttpVerbENUM.GET.value])
def get_experiments(service: ExperimentService):
    """Enpoint - Get experiments. """
    return jsonify([experiment_dto.dump(experiment) for experiment in service.get_all()])

@blueprint.route('/<int:experiment_id>', methods=[HttpVerbENUM.GET.value])
def get_experiment_by_id(service: ExperimentService, experiment_id: int):
    """Enpoint - Get experiment by id. """
    return jsonify(experiment_dto.dump(service.get_by_id(experiment_id)))
