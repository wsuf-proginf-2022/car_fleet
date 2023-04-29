from flask_restful import Resource
from flask_jwt_extended import current_user, jwt_required


class User(Resource):

  @jwt_required()
  def get(self):
    return {'user': current_user.json()}, 200
