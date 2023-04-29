from flask_restful import Resource, reqparse
from models.car import CarModel


class Car(Resource):
  parser = reqparse.RequestParser()
  parser.add_argument('type',
                      type=str,
                      required=True,
                      help='This field cannot be left blank')

  def get(self, plate):
    return {'plate': plate}

  # plate is a path parameter
  def post(self, plate):
    # data from the request body
    data = Car.parser.parse_args()
    print(data)
    car = CarModel(plate, data['type'])
    car.save_to_db()

    return car.json(), 201
