"""Endpoints for handling Experiment data."""
from flask import Blueprint, jsonify, request
from app.commom.enums.http_verb import HttpVerbENUM
from .service import ExperimentService
from .dto import ExperimentDTO, ExperimentPostDTO

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

@blueprint.route('/', methods=[HttpVerbENUM.POST.value])
def register(service: ExperimentService):
    """Enpoint - Register a new experiment """
    experiment_post_dto: ExperimentPostDTO = ExperimentPostDTO()
    
    return jsonify(experiment_dto.dump(service.register(\
        experiment_post_dto.load(request.json))))

@blueprint.route('/<int:experiment_id>', methods=[HttpVerbENUM.DELETE.value])
def delete_experiment_by_id(service: ExperimentService, experiment_id: int):
    """Enpoint - Delete experiment by id. """
    return jsonify(experiment_dto.dump(service.remove(experiment_id)))
