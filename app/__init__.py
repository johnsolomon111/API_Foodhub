from flask_restplus import Api
from flask import Blueprint

from .main.controller.user_controller import api as user_ns
from .main.controller.auth_controller import api as auth_ns
from .main.controller.restaurant_controller import api as rest_ns

blueprint = Blueprint('api', __name__)

api = Api(
  blueprint,
  title='FoodHub API',
  version='1.0',
  description='FoodHub API service'
)

api.add_namespace(user_ns, path='/user')
api.add_namespace(auth_ns, path='/auth')
api.add_namespace(rest_ns, path='/restaurant')