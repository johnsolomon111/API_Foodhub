from app.main import db
from app.main.model.menu import Menu 

def save_new_menu(data,resto_id):
	menu = Menu.query.filter_by(menu_name=data["menu_name"]).first()
	if not menu:
		new_menu = Menu(
			menu_name = data["menu_name"],
			menu_description = data["menu_description"],
			price=data["price"],
			available=data["available"],
			resto_id=resto_id
		)
		save_changes(new_menu)
		response_object = {
			'status': 'success',
			'message': 'Menu Successfully Added'
		}
		return response_object, 200
	else:
		response_object = {
			'status': 'fail',
			'message': 'Menu name already Exists',
		}
		return response_object, 400

def save_changes(data):
	db.session.add(data)
	db.session.commit()

def get_all_menu_by_id(resto_id):
	data = db.session.query(Menu).filter(Menu.resto_id == resto_id).all()
	return data

