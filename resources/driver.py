from flask_restful import Resource, reqparse
from models.driver import DriverModel


class Driver(Resource):
  parser = reqparse.RequestParser()
  parser.add_argument('name',
                      type=str,
                      required=True,
                      help='This field cannot be left blank')

  def post(self):
    data = Driver.parser.parse_args()
    driver = DriverModel(data['name'])
    try:
      driver.save_to_db()
    except:
      return {'message': 'An error occurred inserting the driver.'}, 500

    return driver.json(), 201

  def get(self):
    return {'drivers': [driver.json() for driver in DriverModel.query.all()]}
