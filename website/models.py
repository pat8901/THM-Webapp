from website import db
from flask_login import UserMixin
from sqlalchemy.sql import func

# Database model for hazardous materials.
class Material(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    notes = db.relationship('Note')

# Database model for storing notes on materials.
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True),default=func.now())
    material_id = db.Column(db.Integer, db.ForeignKey('material.id'))

# Database model for Users. Keeps track of users for logging in.
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))