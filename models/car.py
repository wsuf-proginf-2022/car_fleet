from db import db, BaseModel


class CarModel(BaseModel):
  __tablename__ = 'cars'
  id = db.Column(db.Integer, primary_key=True)
  license_plate = db.Column(db.String(7))
  type = db.Column(db.String(50))
