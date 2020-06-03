from .. import db

class Restaurant(db.Model):
	__tablename__ = "restaurant"

	resto_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	resto_name = db.Column(db.String(300), nullable=False)
	location = db.Column(db.String(500), nullable=False)
	sun = db.Column(db.String(20))
	mon = db.Column(db.String(20))
	tue = db.Column(db.String(20))
	wed = db.Column(db.String(20))
	thu = db.Column(db.String(20))
	fri = db.Column(db.String(20))
	sat = db.Column(db.String(20))
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

	def __repr__(self):
		return "<Restaurant '{}'>".format(self.name)

	def __init__(self, resto_name='', location='',sun='',mon='',tue='',wed='',thu='',fri='',sat=''):
		self.resto_name = resto_name
		self.location = location
		self.sun = sun
		self.mon = mon
		self.tue = tue
		self.wed = wed
		self.thu = thu
		self.fri = fri
		self.sat = sat

