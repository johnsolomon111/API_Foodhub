from functools import wraps
from flask_restplus import marshal_with
from flask import request

from app.main.service.auth_helper import Auth

def owner_token_required(f):
  @wraps(f)
  def decorated(*args,**kwargs):
    data, status = Auth.get_logged_in_user(request)
    token = data.get('data')
    print('Data:',data)
    print('status:',status)
    print('token:', token)
    if not token:
      return data, status
    
    return f(*args, **kwargs)
  return decorated

def custom_marshal_with(fields_private, name):
  """
  Customer response marshalling
  """
  def decorated(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
      func = marshal_with(fields_private, envelope=name)(f)
      return func(*args, **kwargs)
    return wrapper
  return decorated