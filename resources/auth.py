from flask_restful import Resource, reqparse
from models.user import UserModel
from flask_jwt_extended import create_access_token
from datetime import timedelta


class Auth(Resource):
  parser = reqparse.RequestParser()
  parser.add_argument('username',
                      type=str,
                      required=True,
                      help='This field cannot be left blank')
  parser.add_argument('password',
                      type=str,
                      required=True,
                      help='This field cannot be left blank')

  def post(self):
    data = Auth.parser.parse_args()
    user = UserModel.find_by_username(data['username'])
    if user and user.password == data['password']:
      access_token = create_access_token(identity=user.id,
                                         expires_delta=timedelta(minutes=30))
      return {'access_token': access_token}, 200
    return {'message': 'Wrong username or password'}, 401
