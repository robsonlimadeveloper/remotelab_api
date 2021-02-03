"""
Code for handling Experiment data..
"""
from injector import inject
from app.core.service_abstract import ServiceAbstract
from .repository import ExperimentRepository
from .model import Experiment
from .dto import ExperimentPostDTO

class ExperimentService(ServiceAbstract):
    """
    Experiment service.
    """
    @inject
    def __init__(self, repository: ExperimentRepository):
        super(ExperimentService, self).__init__(repository)
        self.repository = repository
    
    def register(self, experiment_post_dto: ExperimentPostDTO)-> Experiment:
        """register a new Experiment"""
        return self.repository.save(Experiment(**experiment_post_dto, is_active=True))
