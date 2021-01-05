"""Repository abstract module"""

from typing import List
from multidict import MultiDict
from sqlalchemy import desc, asc
from app import db
from .exceptions_abstract import WrongParameterException, WrongValueParameterException

class RepositoryAbstract:
    """Repository abstract class"""
    session = db.session
    entity: db.Model

    def __init__(self, entity: db.Model):
        """Repository abstract constructor function"""
        self.entity = entity

    def find_all(self) -> List[db.Model]:
        """abstract function find all"""
        return self.session.query(self.entity).all()

    def find_first(self) -> db.Model:
        """abstract function find first"""
        return self.session.query(self.entity).first()

    def find_by_id(self, entity_id: int) -> db.Model:
        """abstract function find by id"""
        return self.session.query(self.entity).filter(self.entity.id == entity_id).first()

    def save(self, model: db.Model) -> db.Model:
        """abstract function save model"""
        self.session.add(model)
        self.session.commit()

        return model

    def update(self, entity_id: int, model: db.Model) -> db.Model:
        """abstract function update model"""
        my_dict = {column: getattr(model, column) for column in model.__table__.columns.keys()}
        del my_dict['id']

        self.session.query(self.entity).filter(self.entity.id == entity_id).update(my_dict)
        self.session.commit()

        return model

    def delete(self, model: db.Model) -> db.Model:
        """abstract function delete model"""
        self.session.delete(model)
        self.session.commit()

        return model

    def find_last(self) -> db.Model:
        """abstract  function find last"""
        return self.session.query(self.entity).order_by(self.entity.id.desc()).first()

    def save_or_update(self, model: db.Model) -> db.Model:
        """abstract function save or update"""
        self.session.merge(model)
        self.session.commit()
