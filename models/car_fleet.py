from db import db, BaseModel
from models.mixin_model import MixinModel
# from sqlalchemy.orm import mapped_column, relationship


class CarFleetLink(BaseModel, MixinModel):
  __tablename__ = 'car_fleet'
  car_id = db.Column(db.Integer, db.ForeignKey('cars.id'), primary_key=True)
  fleet_id = db.Column(db.Integer,
                       db.ForeignKey('fleets.id'),
                       primary_key=True)

  # TODO ezek lehet hogy nem is kellenek
  # car = db.relationship('CarModel', back_populates='fleets')
  # car = relationship('CarModel', back_populates='fleets')
  # fleet = db.relationship('FleetModel', back_populates='cars')
  # fleet = relationship('FleetModel', back_populates='cars')

  def __init__(self, car_id, fleet_id):
    self.car_id = car_id
    self.fleet_id = fleet_id

  @classmethod
  def link_exists(cls, car_id, fleet_id):
    return cls.query.filter_by(car_id=car_id, fleet_id=fleet_id).first()
