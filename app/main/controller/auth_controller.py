from flask import request
from flask_restplus import Resource

from app.main.service.auth_helper import Auth
from ..util.dto import AuthDto

api = AuthDto.api
user_auth = AuthDto.user_auth


@api.route('/login')
class UserLogin(Resource):
    """
        User Login Resource
    """
    @api.doc('user login')
    @api.expect(user_auth, validate=True)
    def post(self):
        # get the post data
        post_data = request.json
        return Auth.login_user(data=post_data)


@api.route('/logout')
class LogoutAPI(Resource):
    """
    Logout Resource
    """
    @api.doc('logout a user')
    def post(self):
        # get auth token
        auth_header = request.headers.get('Authorization')
        return Auth.logout_user(data=auth_header)

@api.route('/logout_customer')
class LogoutAPICus(Resource):
    """
    Logout Resource
    """
    @api.doc('logout a customer')
    def post(self):
        # get auth token
        auth_header = request.headers.get('Authorization')
        return Auth.logout_customer(data=auth_header)

@api.route('/authorize_user')
class GetLoggedIn(Resource):

    @api.doc('get logged in user')
    def post(self):
        auth_token = request.headers.get('Authorization')
        return Auth.get_logged_in_user(auth_token=auth_token)

@api.route('/authorize_customer')
class GetLoggedIn(Resource):

    @api.doc('get logged in customer')
    def post(self):
        auth_token = request.headers.get('Authorization')
        return Auth.get_logged_in_customer(auth_token=auth_token)