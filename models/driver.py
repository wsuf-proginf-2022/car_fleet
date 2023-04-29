from db import db, BaseModel
from sqlalchemy.orm import mapped_column, relationship
from sqlalchemy import Integer, String

from models.mixin_model import MixinModel


class DriverModel(BaseModel, MixinModel):
  __tablename__ = 'drivers'
  # id = db.Column(db.Integer, primary_key=True)
  id = mapped_column(Integer, primary_key=True)
  # name = db.Column(db.String(50))
  name = mapped_column(String(50))

  # bidirectional one-to-one relationship esetén ez is kellene
  # car_id = db.Column(db.Integer, db.ForeignKey('cars.id'))

  car = relationship('CarModel', back_populates='driver', uselist=False)

  def __init__(self, name):
    self.name = name

  def json(self):
    return {'name': self.name, 'id': self.id}

  @classmethod
  def find_by_id(cls, id):
    return cls.query.filter_by(id=id).first()
