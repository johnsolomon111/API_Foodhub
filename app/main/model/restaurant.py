import datetime

from .. import db
from app.main.model import user

class Restaurant(db.Model):
  """ Restaurant Model for storing restaurant related details """

  __tablename__ = "restaurant"

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  restaurant_name = db.Column(db.String(100), nullable=False, unique=True)
  restaurant_type = db.Column(db.String(125), nullable=False)
  business_hours = db.Column(db.String(50), nullable=False)
  location = db.Column(db.String(100), nullable=False)
  contact_number = db.Column(db.String(15), nullable=False)
  telephone_number = db.Column(db.String(15), nullable=False)
  date_created = db.Column(db.DateTime, nullable=False)
  restaurant_owner = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

  def __repr__(self):
    return "<Restaurant '{}'>".format(self.restaurant_name)
  
  def add(data):
    db.session.add(data)
    db.session.commit()