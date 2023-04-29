from models.car import CarModel
from models.driver import DriverModel
from flask_restful import Resource, reqparse
from db import db


class AssignDriverToCar(Resource):
  parser = reqparse.RequestParser()
  parser.add_argument('driver_id',
                      type=int,
                      required=True,
                      help='This field cannot be left blank')
  parser.add_argument('car_id',
                      type=int,
                      required=True,
                      help='This field cannot be left blank')

  def post(self):
    data = AssignDriverToCar.parser.parse_args()
    driver = DriverModel.find_by_id(data['driver_id'])

    # if driver:
    #   if car:
    #     if car.driver_id == driver.id:
    #       other_driver = db.session.query(CarModel).filter(
    #           CarModel.driver_id == driver.id).first()
    #       if not other_driver:
    #         if car.driver_id is None:
    #           car.driver_id = driver.id
    #           db.session.commit()
    #           return {
    #               'message':
    #               f"Driver {driver.name} was assigned to car: {car.license_plate}."
    #           }, 201
    #         else:
    #           return {'message': 'Car already has a driver.'}, 400
    #       else:
    #         return {
    #             'message':
    #             f"Driver {driver.name} is already assigned to another car!"
    #         }, 400
    #     else:
    #       return {'message': 'Driver already assigned to car.'}, 400
    #   else:
    #     return {'message': 'Car not found.'}, 404

    if not driver:
      return {'message': 'Driver not found.'}, 404

    car = CarModel.find_by_id(data['car_id'])
    if not car:
      return {'message': 'Car not found.'}, 404

    if car.driver_id == driver.id:
      return {'message': 'This car is already assigned to another driver'}, 400

    other_driver = db.session.query(CarModel).filter(
        CarModel.driver_id == driver.id).first()

    if other_driver:
      return {
          'message': f"This driver is already assigned to another car"
      }, 400

    if car.driver_id is not None:
      return {'message': 'Car already has a driver.'}, 400

    # ha ide eljutunk, akkor a driver és a car is létezik, és a car-nak nincs
    # driver-je, illetve a driver-nek nincs car-ja, tehát hozzárendelhetjük:
    car.driver_id = driver.id
    # bidirectional one-to-one relationship esetén ez is kellene
    # driver.car_id = car.id
    db.session.commit()

    return {
        'message':
        f"Driver {driver.name} was assigned to car: {car.license_plate}."
    }, 201
