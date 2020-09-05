from flask import request
from flask_restplus import Resource

from app.main.util.dto import UserDto
from app.main.util.custom_dto import UserDtoPublic
from app.main.service.user_service import create_user, create_customer, create_owner, get_all_users, get_all_owners, get_all_customer
from app.main.util.decorator import owner_token_required, custom_marshal_with

api = UserDto.api
_user = UserDto.user

@api.route('/sign-up')
class CreateUser(Resource):
  @api.response(201, 'User successfully created!')
  @api.doc('create a user')
  @api.expect(_user, validate=True)
  def post(self):
    """ Register a user. """
    data = request.json
    return create_user(data=data)

@api.route('/customer/sign-up')
class CreateCustomer(Resource):
  @api.response(201, 'Customer successfully created!')
  @api.doc('create a customer')
  @api.expect(_user, validate=True)
  def post(self):
    """ Register a customer. """
    data = request.json
    return create_customer(data=data)
  
@api.route('/owner/sign-up')
class CreateOwner(Resource):
  @api.response(201, 'Owner successfully created!')
  @api.doc('create a owner')
  @api.expect(_user, validate=True)
  def post(self):
    """ Register a Owner. """
    data = request.json
    return create_owner(data=data)

@api.route('/all')
class GetUser(Resource):
  @api.doc('get all users')
  # @owner_token_required
  @custom_marshal_with(UserDtoPublic, name="Users")
  def get(self):
    """ Return all users. """
    return get_all_users()

@api.route('/customer/all')
class GetAllCustomer(Resource):
  @api.doc('get all customers')
  @custom_marshal_with(UserDtoPublic, name="Customers")
  def get(self):
    """ Return all customers """
    return get_all_customer()

@api.route('/owner/all')
class GetAllOwner(Resource):
  @api.doc('get all owners')
  @custom_marshal_with(UserDtoPublic, name="Owners")
  def get(self):
    """ Return all owners """
    return get_all_owners()