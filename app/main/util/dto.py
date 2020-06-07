from flask_restplus import Namespace, fields


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'password': fields.String(required=True, description='user password'),
        'phone_number': fields.String(description='user Identifier'),
        'name': fields.String(description='user full name')
    })

class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
    })

class CustomerDto:
    api = Namespace('customer', description='customer related operations')
    customer = api.model('customer', {
        'email': fields.String(required=True, description='user email address'),
        'password': fields.String(required=True, description='user password'),
        'phone_number': fields.String(description='user Identifier'),
        'customer_name': fields.String(description='customer full name')
    })

class RestaurantDto:
    api = Namespace('restaurant', description='restaurant realated operations')
    restaurant = api.model('restaurant', {
        'resto_id': fields.String(description='resto identification'),
        'resto_name': fields.String(required=True, description='business name'),
        'location': fields.String(required=True,description='business location'),
        'resto_description': fields.String(required=True, description='paragraph for business'),
        'services': fields.String(description='what business has to offer'),
        'sun': fields.String(description='operation hours'),
        'mon': fields.String(description='operation hours'),
        'tue': fields.String(description='operation hours'),
        'wed': fields.String(description='operation hours'),
        'thu': fields.String(description='operation hours'),
        'fri': fields.String(description='operation hours'),
        'sat': fields.String(description='operation hours')
        })

class MenuDto:
    api = Namespace('menu', description='menu related operations')
    menu = api.model('menu', {
        'menu_id': fields.String(description='menu identification'),
        'menu_name' : fields.String(required=True, description='dish name'),
        'menu_description': fields.String(description='dish description'),
        'price':fields.String(description='dish price'),
        'available': fields.Boolean(description='dish availability')
        })