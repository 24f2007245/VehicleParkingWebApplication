from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
from datetime import datetime

class UserData(db.Model):
    __tablename__='user_data'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    user_name = db.Column(db.String(60), nullable=False)
    user_email = db.Column(db.String(130),unique=True, nullable=False)
    password= db.Column(db.String(200), nullable=False)
    vehicle_no = db.Column(db.String(20))
    address = db.Column(db.String(200), nullable=True)  # Optional address field
    roles = db.Column(db.String(20), default='user')  # Default role is 'user'

class ParkingLot(db.Model):
    __tablename__='parking_lot'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    lot_name = db.Column(db.String(60), nullable=True)
    location = db.Column(db.String(100), nullable=True)
    pin_code = db.Column(db.String(10), nullable=False)
    price = db.Column(db.Float, nullable=False)
    address = db.Column(db.String(200), nullable=True)  # Optional address field
    total_slots = db.Column(db.Integer(), nullable=False)
    available_slots = db.Column(db.Integer())



class ParkingSpot(db.Model):
    __tablename__='parking_spot'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    lot_id = db.Column(db.Integer(), db.ForeignKey('parking_lot.id'))
    status = db.Column(db.String(20), nullable=False)  
    # vehicle_number = db.Column(db.String(20), nullable=True)  

class ReservedSpot(db.Model):
    __tablename__='reserved_spot'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    spot_id = db.Column(db.Integer(),db.ForeignKey('parking_spot.id'))
    user_id = db.Column(db.Integer(), db.ForeignKey('user_data.id'))
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)
    parking_cost = db.Column(db.Float, nullable=False)
