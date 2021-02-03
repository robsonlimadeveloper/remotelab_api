"""
Code for handling Experiment Session data..
"""
from injector import inject
from app.core.service_abstract import ServiceAbstract
from .repository import ExperimentSessionRepository
from .model import ExperimentSession
from .dto import ExperimentSessionPostDTO

class ExperimentSessionService(ServiceAbstract):
    """
    ExperimentSession service.
    """
    @inject
    def __init__(self, repository: ExperimentSessionRepository):
        super(ExperimentSessionService, self).__init__(repository)
        self.repository = repository
    
    def register(self, experiment_session_post_dto: ExperimentSessionPostDTO)-> ExperimentSession:
        return self.repository.save(ExperimentSession(**experiment_session_post_dto,\
            is_active=True))
