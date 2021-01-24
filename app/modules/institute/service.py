"""
Code for handling institute data..
"""
from injector import inject
from app.core.service_abstract import ServiceAbstract
from .repository import InstituteRepository
from .model import Institute

class InstituteService(ServiceAbstract):
    """
    Institute service.
    """
    @inject
    def __init__(self, repository: InstituteRepository):
        super(InstituteService, self).__init__(repository)
        self.repository = repository