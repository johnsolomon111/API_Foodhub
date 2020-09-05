from flask_restplus import Model, fields

UserDtoPublic = Model('user_public', {
  'public_id' : fields.String(),
  'full_name' : fields.String(),
  'email' : fields.String(),
  'contact_number' : fields.String(),
  'registered_on' : fields.String(),
  'user_type' : fields.String()
})

RestaurantDtoPublic = Model('restaurant_public', {
  'restaurant_name': fields.String(),
        'restaurant_type': fields.String(),
        'business_hours': fields.String(),
        'location': fields.String(),
        'contact_number': fields.String(),
        'telephone_number': fields.String(),
        'date_created': fields.String(),
        'restaurant_owner': fields.String()
})