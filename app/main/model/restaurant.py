from .. import db
from app.main.model.menu import *


class Restaurant(db.Model):
	__tablename__ = "restaurant"

	resto_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	resto_name = db.Column(db.String(300), nullable=False, unique=True)
	location = db.Column(db.String(500), nullable=False)
	resto_description = db.Column(db.String(500))
	services = db.Column(db.String(500))
	sun = db.Column(db.String(20))
	mon = db.Column(db.String(20))
	tue = db.Column(db.String(20))
	wed = db.Column(db.String(20))
	thu = db.Column(db.String(20))
	fri = db.Column(db.String(20))
	sat = db.Column(db.String(20))
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	menus = db.relationship('Menu',backref='resto_menu')

	def __repr__(self):
		return "<Restaurant '{}'>".format(self.resto_name)

	def __init__(self,user_id='', resto_name='',services='',resto_description='', location='',sun='',mon='',tue='',wed='',thu='',fri='',sat=''):
		self.resto_name = resto_name
		self.location = location
		self.resto_description = resto_description
		self.sun = sun
		self.mon = mon
		self.tue = tue
		self.wed = wed
		self.thu = thu
		self.fri = fri
		self.sat = sat
		self.services = services
		self.user_id=user_id




