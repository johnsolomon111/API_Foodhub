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
    api = Namespace('customer', description='user related operations')
    customer = api.model('customer', {
        'email': fields.String(required=True, description='user email address'),
        'password': fields.String(required=True, description='user password'),
        'phone_number': fields.String(description='user Identifier'),
        'customer_name': fields.String(description='customer full name')
    })