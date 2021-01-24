"""
Code for handling Discipline Type data..
"""
from injector import inject
from app.core.service_abstract import ServiceAbstract
from .repository import DisciplineTypeRepository
from .model import DisciplineType

class DisciplineTypeService(ServiceAbstract):
    """
    DisciplineType service.
    """
    @inject
    def __init__(self, repository: DisciplineTypeRepository):
        super(DisciplineTypeService, self).__init__(repository)
        self.repository = repository