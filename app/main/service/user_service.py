import uuid
import datetime

from app.main import db
from app.main.model.user import User

def create_user(data):
  user = User.query.filter_by(email=data['email']).first()
  if not user:
    new_user = User(
      public_id = str(uuid.uuid4())[:8],
      email = data['email'],
      full_name = data['full_name'],
      password = data['password'],
      contact_number = data['contact_number'],
      user_type = data['user_type'],
      registered_on = datetime.datetime.utcnow()
    )
    add_user(new_user)
    return generate_token(new_user)
  else:
    response_object = {
      'status':'fail',
      'message':'User already exists. Please login.'
    }
    return response_object, 409

def create_owner(data):
  user = User.query.filter_by(email=data['email']).first()
  if not user:
    new_user = User(
      public_id = str(uuid.uuid4())[:8],
      email = data['email'],
      full_name = data['full_name'],
      password = data['password'],
      contact_number = data['contact_number'],
      user_type = 'Owner',
      registered_on = datetime.datetime.utcnow()
    )
    add_user(new_user)
    return generate_token(new_user)
  else:
    response_object = {
      'status':'fail',
      'message':'User already exists. Please login.'
    }
    return response_object, 409

def create_customer(data):
  user = User.query.filter_by(email=data['email']).first()
  if not user:
    new_user = User(
      public_id = str(uuid.uuid4())[:8],
      email = data['email'],
      full_name = data['full_name'],
      password = data['password'],
      contact_number = data['contact_number'],
      user_type = 'Customer',
      registered_on = datetime.datetime.utcnow()
    )
    add_user(new_user)
    return generate_token(new_user)
  else:
    response_object = {
      'status':'fail',
      'message':'User already exists. Please login.'
    }
    return response_object, 409

def get_all_users():
  return User.query.all()

def get_all_owners():
  return User.query.filter_by(user_type='Owner').all()

def get_all_customer():
  return User.query.filter_by(user_type='Customer').all()  

def add_user(data):
  db.session.add(data)
  db.session.commit()

def generate_token(user):
  try:
    auth_token = user.encode_auth_token(user.id)
    response_object = {
      'status':'success',
      'message':'User successfully registered.',
      'Authorization': auth_token.decode()
    }
    return response_object, 201
  except Exception as e:
    response_object = {
      'status':'fail',
      'message':'Some error occurred. Please try again.'
    }
    return response_object, 401