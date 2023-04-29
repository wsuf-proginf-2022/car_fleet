from db import db, BaseModel
from sqlalchemy.orm import mapped_column, relationship
from sqlalchemy import Integer, String, ForeignKey


class FleetModel(BaseModel):
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
