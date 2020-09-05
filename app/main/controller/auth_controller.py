from flask import request
from flask_restplus import Resource

from app.main.service.auth_helper import Auth
from ..util.dto import AuthDto

api = AuthDto.api
user_auth = AuthDto.user_auth

@api.route('/login')
class UserLogin(Resource):
  """
  User login resource.
  """
  @api.doc('user login')
  @api.expect(user_auth,validate=True)
  def post(self):
    post_data = request.json
    return Auth.login_user(data=post_data)

@api.route('/logout')
class UserLogout(Resource):
  """
  User logout resource.
  """
  @api.doc('user logout')
  def post(self):
    auth_header = request.headers.get('Authorization')
    print(auth_header)
    return Auth.logout_user(data=auth_header)
  
@api.route('/user')
class AuthUser(Resource):
  """
  Authorize Current User
  """
  @api.doc('authorize user')
  def post(self):
    token = request.headers.get('Authorization')
    return Auth.authorize_user(auth_token=token)