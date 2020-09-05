from flask_restplus import Namespace, fields

class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
    })

class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'full_name': fields.String(required=True, description='user full name'),
        'email': fields.String(required=True, description='user email address'),
        'password': fields.String(required=True, description='user password'),
        'contact_number': fields.String(required=True, description='user contact number')
    })

class RestaurantDto:
    api = Namespace('restaurant', description='restaurant related operatios')
    restaurant = api.model('restaurant',{
        'restaurant_name': fields.String(required=True, description='restaurant name'),
        'restaurant_type': fields.String(required=True, description='restaurant type'),
        'business_hours': fields.String(required=True, description='restaurant business hours'),
        'location': fields.String(required=True, description='restaurant location'),
        'contact_number': fields.String(required=True, description='restaurant contact_number'),
        'telephone_number': fields.String(required=True, description='restaurant telephone_number')
    })