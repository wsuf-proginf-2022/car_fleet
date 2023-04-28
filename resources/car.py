from flask_restful import Resource


class Car(Resource):

  def get(self, plate):
    return {'plate': plate}
