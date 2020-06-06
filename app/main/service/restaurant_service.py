from app.main import db
from app.main.model.restaurant import Restaurant 

def save_new_restaurant(data,user_id):
	print(user_id)
	restaurant = Restaurant.query.filter_by(resto_name=data["resto_name"]).first()
	if not restaurant:
		new_restaurant = Restaurant(
			resto_name=data['resto_name'],
			location=data['location'],
			resto_description=data['resto_description'],
			services=data['services'],
			sun=data['sun'],
			mon=data['mon'],
			tue=data['tue'],
			wed=data['wed'],
			thu=data['thu'],
			fri=data['fri'],
			sat=data['sat'],
			user_id=user_id
		)
		save_changes(new_restaurant)
		response_object = {
			'status':'success',
			'message': 'Restaurant Successfully Added'
		}
		return response_object, 200
	else:
		response_object = {
			'status':'fail',
			'message': 'Restaurant name already exists',
		}
		return response_object, 409


def save_changes(data):
	db.session.add(data)
	db.session.commit()

def get_all_resto_by_owner(user_id):
	data = db.session.query(Restaurant).filter(Restaurant.user_id == user_id).all()
	print(data)
	return data

def get_a_restaurnt(resto_name):
	return Restaurant.query.filter_by(resto_name=resto_name).first()