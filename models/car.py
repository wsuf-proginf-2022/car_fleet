from db import db, BaseModel
from sqlalchemy.orm import mapped_column, relationship
from sqlalchemy import Integer, String
from sqlalchemy import ForeignKey


class CarModel(BaseModel):
  __tablename__ = 'cars'
  # id = db.Column(db.Integer, primary_key=True)
  id = mapped_column(Integer, primary_key=True)
  # license_plate = db.Column(db.String(7), unique=True)
  license_plate = mapped_column(String(7), unique=True)
  # type = db.Column(db.String(50))
  type = mapped_column(String(50))
  driver_id = mapped_column(Integer, ForeignKey('drivers.id'), unique=True)

  driver = relationship('DriverModel', back_populates='car', uselist=False)

  def __init__(self, license_plate, type):
    self.license_plate = license_plate
    self.type = type

  def save_to_db(self):
    db.session.add(self)
    db.session.commit()

  def delete_from_db(self):
    db.session.delete(self)
    db.session.commit()

  @classmethod
  def find_by_id(cls, id):
    return cls.query.filter_by(id=id).first()

  @classmethod
  def find_by_plate(cls, license_plate):
    return cls.query.filter_by(license_plate=license_plate).first()

  def json(self):
    return {
        'license_plate': self.license_plate,
        'type': self.type,
        'id': self.id
    }
