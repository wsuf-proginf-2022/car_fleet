from flask import Flask
from flask_restful import Api
import os

from models.car import CarModel
from models.driver import DriverModel
from models.fleet import FleetModel
from models.car_fleet import CarFleetLink

from resources.car import Car, CarList
from resources.driver import Driver
from resources.assign import AssignDriverToCar
from resources.car_fleet import CarFleet
from resources.fleet import Fleet, FleetList
from db import db

app: Flask = Flask(__name__)
api: Api = Api(app)
db_path: str = os.path.join(os.path.dirname(__file__), 'data.db')
db_uri: str = f'sqlite:///{db_path}'

app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


# before_first_request: ez a dekorátor akkor fut le, amikor az első kérés érkezik a szerverhez
@app.before_first_request
def create_tables() -> None:
  # létrehozza az összes táblát, amelyet a models mappában definiáltunk
  db.create_all()


api.add_resource(Car, '/car/<string:plate>')
api.add_resource(CarList, '/cars')
api.add_resource(Driver, '/driver')
api.add_resource(AssignDriverToCar, '/assign')
api.add_resource(CarFleet, '/car_fleet')
api.add_resource(Fleet, '/fleet/<string:name>')
api.add_resource(FleetList, '/fleets')
