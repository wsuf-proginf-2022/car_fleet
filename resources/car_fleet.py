from flask_restful import Resource, reqparse
from models.car import CarModel
from models.fleet import FleetModel
from models.car_fleet import CarFleetLink


class CarFleet(Resource):
  parser = reqparse.RequestParser()
  parser.add_argument('car_id',
                      type=int,
                      required=True,
                      help='This field cannot be left blank')
  parser.add_argument('fleet_id',
                      type=int,
                      required=True,
                      help='This field cannot be left blank')

  def post(self):
    data = CarFleet.parser.parse_args()
    car = CarModel.find_by_id(data['car_id'])
    fleet = FleetModel.find_by_id(data['fleet_id'])

    if not car:
      return {'message': 'Car not found.'}, 404

    if not fleet:
      return {'message': 'Fleet not found.'}, 404

    if CarFleetLink.link_exists(car.id, fleet.id):
      return {'message': 'Car already assigned to fleet.'}, 400

    car_fleet_link = CarFleetLink(car.id, fleet.id)
    car_fleet_link.save_to_db()

    return {'message': 'Car assigned to fleet.'}, 201
