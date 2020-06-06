from flask import request
from flask_restplus import Resource

from ..util.dto import RestaurantDto
from ..service.restaurant_service import save_new_restaurant,get_all_resto_by_owner

api = RestaurantDto.api
_restaurant = RestaurantDto.restaurant

@api.route('/<user_id>')
class RestaurantList(Resource):
	@api.doc('list of restaurants owned by user')
	@api.marshal_list_with(_restaurant, envelope='data')
	def get(self,user_id):
		restos = get_all_resto_by_owner(user_id)
		print(restos)
		return restos

	@api.response(201, 'Restaurant successfully created')
	@api.doc('create new restaurant')
	@api.expect(_restaurant, validate=True)
	def post(self,user_id):
		data = request.json
		print('user_id: ' + str(user_id))
		return save_new_restaurant(data=data,user_id=user_id)
