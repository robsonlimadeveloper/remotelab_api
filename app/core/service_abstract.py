"""Service abstract to manage the models data."""
from typing import List
from marshmallow import Schema
from app import db
from .repository_abstract import RepositoryAbstract
from ..commom.exceptions.information_not_found import InformationNotFound

class ServiceAbstract:
    """Abstract class"""
    repository: RepositoryAbstract

    def __init__(self, repository: RepositoryAbstract):
        self.repository = repository

    def get_by_id(self, id_model: int) -> db.Model:
        """GET model by id"""
        instance = self.repository.find_by_id(id_model)

        if not instance:
            raise InformationNotFound

        return self.repository.find_by_id(id_model)

    def register(self, dto: Schema) -> db.Model:
        """Save a new model in db."""
        return self.repository.save(db.Model(**dto))

    def update(self, id_model: int, dto: Schema) -> db.Model:
        """Updates an existing model."""
        return self.repository.update(id_model, db.Model(**dto))

    def remove(self, id_model: int) -> db.Model:
        """Remove an existing model."""
        instance: db.Model = self.get_by_id(id_model)

        return self.repository.delete(instance)

    def get_last(self) -> db.Model:
        """Get last existing model."""
        instance = self.repository.find_last()

        if not instance:
            raise InformationNotFound

        return instance

    def get_all(self) -> List[db.Model]:
        """Get all models"""
        return self.repository.find_all()

    def get_first(self, args: dict) -> db.Model:
        """Get first model"""
        return self.repository.find_first()
