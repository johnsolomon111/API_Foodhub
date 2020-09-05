from flask import request
from flask_restplus import Resource

from app.main.util.dto import RestaurantDto
from app.main.util.custom_dto import RestaurantDtoPublic
from app.main.util.decorator import custom_marshal_with
from app.main.service.auth_helper import Auth
from app.main.service.restaurant_service import add_restaurant, get_restaurants

api = RestaurantDto.api
_restaurant = RestaurantDto.restaurant


@api.route('/')
class RestaurantList(Resource):
  @api.doc('return all restaurant')
  @custom_marshal_with(RestaurantDtoPublic, name="Restaurants")
  def get(self):
    """ get all restaurants """
    current_user = Auth.get_logged_in_user(request)
    return get_restaurants(owner_id=current_user[0]['data']['id'])

@api.route('/add')
class Restaurant(Resource):
  @api.response(201,'Restaurant successfully created')
  @api.doc('create a restaurant')
  @api.expect(_restaurant, validate=True)
  def post(self):
    """ create a new restaurant """
    data = request.json
    current_user = Auth.get_logged_in_user(request)
    return add_restaurant(data=data, owner_id=current_user[0]['data']['id'])
  