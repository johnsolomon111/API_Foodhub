import datetime

from app.main import db
from app.main.model.restaurant import Restaurant

def add_restaurant(data, owner_id):
  restaurant = Restaurant.query.filter_by(restaurant_name=data['restaurant_name']).first()
  if not restaurant:
    new_restaurant = Restaurant(
      restaurant_name = data['restaurant_name'],
      restaurant_type = data['restaurant_type'],
      business_hours = data['business_hours'],
      location = data['location'],
      contact_number = data['contact_number'],
      telephone_number = data['telephone_number'],
      date_created = datetime.datetime.utcnow(),
      restaurant_owner = owner_id
    )
    Restaurant.add(new_restaurant)
    response_object = {
      'status':'success',
      'message':'Restaurant successfully created'
    }
    return response_object, 201
  else:
    response_object = {
      'status':'fail',
      'message':'Restaurant already exists.'
    }
    return response_object, 409

def get_restaurants(owner_id):
  return Restaurant.query.filter_by(restaurant_owner=owner_id).all()