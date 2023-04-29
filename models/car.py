from db import db, BaseModel


class CarModel(BaseModel):
  __tablename__ = 'cars'
  id = db.Column(db.Integer, primary_key=True)
  license_plate = db.Column(db.String(7))
  type = db.Column(db.String(50))

  def __init__(self, license_plate, type):
    self.license_plate = license_plate
    self.type = type

  def save_to_db(self):
    db.session.add(self)
    db.session.commit()

  def json(self):
    return {'license_plate': self.license_plate, 'type': self.type}
