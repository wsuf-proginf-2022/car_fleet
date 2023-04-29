from db import db, BaseModel
from sqlalchemy.orm import mapped_column, relationship
from sqlalchemy import Integer, String, ForeignKey

from models.mixin_model import MixinModel


class FleetModel(BaseModel, MixinModel):
  __tablename__ = 'fleets'
  # id = db.Column(db.Integer, primary_key=True)
  id = mapped_column(Integer, primary_key=True)
  # name = db.Column(db.String(50))
  name = mapped_column(String(50))

  # many-to-many relationship
  # cars = db.relationship('CarFleetLink', back_populates='fleet')
  cars = relationship('CarModel',
                      secondary='car_fleet',
                      back_populates='fleets')

  def __init__(self, name):
    self.name = name

  @classmethod
  def find_by_id(cls, id):
    return cls.query.filter_by(id=id).first()

  @classmethod
  def find_by_name(cls, name):
    return cls.query.filter_by(name=name).first()

  def json(self, include_cars=True):
    fleet = {'name': self.name, 'id': self.id}
    if include_cars:
      fleet['cars'] = [car.json(include_fleets=False) for car in self.cars]
    return fleet
