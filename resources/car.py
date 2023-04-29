from flask_restful import Resource, reqparse
from models.car import CarModel
from flask_jwt_extended import jwt_required


class Car(Resource):
  parser = reqparse.RequestParser()
  parser.add_argument('type',
                      type=str,
                      required=True,
                      help='This field cannot be left blank')

  def get(self, plate):
    car = CarModel.find_by_plate(plate)
    if car:
      return car.json()
    return {'message': 'Car not found'}, 404

  # plate is a path parameter
  def post(self, plate):
    if CarModel.find_by_plate(plate):
      return {
          'message': "A car with plate '{}' already exists.".format(plate)
      }, 400

    if not plate[0:3].isalpha() or not plate[4:7].isdigit() or not len(
        plate) == 7:
      return {'message': 'Plate must be hungarian format: ABC-123'}, 400

    # data from the request body
    data = Car.parser.parse_args()
    print(data)
    car = CarModel(plate, data['type'])
    try:
      car.save_to_db()
    except:
      return {'message': 'An error occurred inserting the car.'}, 500

    return car.json(), 201

  def delete(self, plate):
    # car = CarModel.query.filter_by(license_plate=plate).first()
    car = CarModel.find_by_plate(plate)
    if car:
      car.delete_from_db()
      return {'message': 'Car deleted'}

    return {'message': 'Car not found.'}, 404

  def put(self, plate):
    data = Car.parser.parse_args()

    car = CarModel.find_by_plate(plate)

    if car:
      car.type = data['type']
      car.save_to_db()
    else:
      return {'message': 'Car not found.'}, 404

    return car.json()


class CarList(Resource):

  @jwt_required()
  def get(self):
    return {'cars': [car.json() for car in CarModel.query.all()]}
