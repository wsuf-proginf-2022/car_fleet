from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_cors import CORS
import os

from models.car import CarModel
from models.driver import DriverModel
from models.fleet import FleetModel
from models.car_fleet import CarFleetLink
from models.user import UserModel

from resources.car import Car, CarList
from resources.driver import Driver
from resources.assign import AssignDriverToCar
from resources.car_fleet import CarFleet
from resources.fleet import Fleet, FleetList
from resources.register import UserRegister
from resources.auth import Auth
from resources.user import User
from db import db

db_path: str = os.path.join(os.path.dirname(__file__), 'data.db')
db_uri: str = f'sqlite:///{db_path}'

# create database car_fleet;
# create user 'car_fleet'@'localhost' identified by '12345';
# grant all privileges on car_fleet.* to 'car_fleet'@'localhost';
# flush privileges;

# pip install mysqlclient
# db_uri: str = f'mysql+mysqldb://car_fleet:12345@localhost:3306/car_fleet'

app: Flask = Flask(__name__)

app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this!
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api: Api = Api(app)
jwt: JWTManager = JWTManager(app)
CORS(app)

db.init_app(app)


# before_first_request: ez a dekorátor akkor fut le, amikor az első kérés érkezik a szerverhez
@app.before_first_request
def create_tables() -> None:
  # létrehozza az összes táblát, amelyet a models mappában definiáltunk
  db.create_all()


# Register a callback function that loads a user from your database whenever
# a protected route is accessed. This should return any python object on a
# successful lookup, or None if the lookup failed for any reason (for example
# if the user has been deleted from the database).
@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
  identity = jwt_data["sub"]
  print(f"identity: {identity}")
  return UserModel.find_by_id(id=identity)


api.add_resource(Car, '/car/<string:plate>')
api.add_resource(CarList, '/cars')
api.add_resource(Driver, '/driver')
api.add_resource(AssignDriverToCar, '/assign')
api.add_resource(CarFleet, '/car_fleet')
api.add_resource(Fleet, '/fleet/<string:name>')
api.add_resource(FleetList, '/fleets')
api.add_resource(UserRegister, '/register')
api.add_resource(Auth, '/auth')
api.add_resource(User, '/user')
