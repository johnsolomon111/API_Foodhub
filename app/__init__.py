
# app/__init__.py

from flask_restplus import Api
from flask import Blueprint

from .main.controller.user_controller import api as user_ns
from .main.controller.customer_controller import api as customer_ns
from .main.controller.restaurant_controller import api as restaurant_ns
from .main.controller.menu_controller import api as menu_ns
from .main.controller.auth_controller import api as auth_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='FLASK RESTPLUS API BOILER-PLATE WITH JWT',
          version='1.0',
          description='a boilerplate for flask restplus web service'
          )

api.add_namespace(user_ns, path='/user')
api.add_namespace(customer_ns, path='/customer')
api.add_namespace(restaurant_ns, path='/restaurant')
api.add_namespace(auth_ns)
api.add_namespace(menu_ns, path='/menu')