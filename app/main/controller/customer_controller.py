from flask import request
from flask_restplus import Resource

from ..util.dto import CustomerDto
from ..service.customer_service import save_new_customer, get_all_customer, get_a_customer

api = CustomerDto.api
_user = CustomerDto.customer


@api.route('/')
class CustomerList(Resource):
    @api.doc('list_of_registered_customer')
    @api.marshal_list_with(_user, envelope='data')
    def get(self):
        """List all registered users"""
        return get_all_customer()

    @api.response(201, 'Customer successfully created.')
    @api.doc('create a new customer')
    @api.expect(_user, validate=True)
    def post(self):
        """Creates a new User """
        data = request.json
        return save_new_customer(data=data)


@api.route('/<customer_id>')
@api.param('customer_id', 'The Customer identifier')
@api.response(404, 'Customer not found.')
class User(Resource):
    @api.doc('get a customer')
    @api.marshal_with(_user)
    def get(self, customer_id):
        """get a user given its identifier"""
        user = get_a_customer(customer_id)
        if not user:
            api.abort(404)
        else:
            return user