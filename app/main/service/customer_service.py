import uuid
import datetime

from app.main import db
from app.main.model.customer import Customer


def save_new_customer(data):
    customer = Customer.query.filter_by(email=data['email']).first()
    if not customer:
        new_customer = Customer(
            email=data['email'],
            phone_number=data['phone_number'],
            password=data['password'],
            customer_name=data['customer_name'],
            registered_on=datetime.datetime.utcnow()
        )
        save_changes(new_customer)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.'
        }
        return generate_token(new_customer)
    else:
        response_object = {
            'status': 'fail',
            'message': 'Email already exists. Please Log in.',
        }
        return response_object, 409


def get_all_customer():
    return Customer.query.all()


def get_a_customer(customer_id):
    return Customer.query.filter_by(customer_id=customer_id).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()

def generate_token(customer):
    try:
        # generate the auth token
        auth_token = customer.encode_auth_token(customer.customer_id)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.',
            'Authorization': auth_token.decode()
        }
        return response_object, 201
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401