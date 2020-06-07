from flask import request
from flask_restplus import Resource

from ..util.dto import MenuDto
from ..service.menu_service import save_new_menu, get_all_menu_by_id

api = MenuDto.api
_menu = MenuDto.menu 

@api.route('/<resto_id>')
class MenuList(Resource):
	@api.doc('list all dishes in this resto')
	@api.marshal_list_with(_menu, envelope='data')
	def get(self, resto_id):
		menus = get_all_menu_by_id(resto_id)
		return menus

	@api.response(201, 'Menu Successfully Created')
	@api.doc('create new menu')
	@api.expect(_menu, validate=True)
	def post(seld,resto_id):
		data = request.json
		return save_new_menu(data=data, resto_id=resto_id)