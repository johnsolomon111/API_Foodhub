from .. import db

class Menu(db.Model):
	__tablename__="menu"

	menu_id = db.Column(db.Integer, primary_key=True,autoincrement=True)
	menu_name = db.Column(db.String(100), nullable=False)
	menu_description = db.Column(db.String(500))
	price = db.Column(db.String(20), nullable=True)
	available = db.Column(db.Boolean,nullable=True, default=True)
	resto_id = db.Column(db.Integer, db.ForeignKey('restaurant.resto_id'))

	def __repr__(self):
		return "<Menu '{}'>".format(self.menu_name)

	def __init__(self,menu_name='',resto_id='',menu_description='', price='',available=''):
		self.menu_name = menu_name
		self.menu_description = menu_description
		self.price = price
		self.available = available
		self.resto_id = resto_id
