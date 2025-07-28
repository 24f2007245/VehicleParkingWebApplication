from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
db = SQLAlchemy()

class UserData(db.Model):
    __tablename__='user_data'
    id = db.Column(db.Integer(), primary_key =True, autoincrement=True)
    user_name = db.Column(db.String(60), nullable =False)
    user_email = db.Column(db.String(130),unique =True, nullable=False)
    password= db.Column(db.String(200), nullable =False)    
    address = db.Column(db.String(200), nullable =True)  
    roles = db.Column(db.String(20), default ='user')  

    reservations=db.relationship('ReservedSpot',backref='users',lazy=True)


class ParkingLot(db.Model):
    __tablename__='parking_lot'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    lot_name = db.Column(db.String(60), nullable=False)
    pin_code = db.Column(db.Integer(), nullable=False)
    price = db.Column(db.Integer(), nullable=False,)
    address = db.Column(db.String(200), nullable=False)  
    total_spots = db.Column(db.Integer(), nullable=False) #price per ghanta me h
    reserved_spots = db.Column(db.Integer(), default=0)

    spots=db.relationship('ParkingSpot',backref='parking_lot', lazy=True)

class ParkingSpot(db.Model):
    __tablename__='parking_spot'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    lot_id = db.Column(db.Integer(), db.ForeignKey('parking_lot.id'))
    status = db.Column(db.Integer(), nullable=False, default=0)  # 0-available and 1-nota

    reservations=db.relationship('ReservedSpot',backref='spot',lazy=True)

class ReservedSpot(db.Model):
    __tablename__='reserved_spot'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    spot_id = db.Column(db.Integer(),db.ForeignKey('parking_spot.id'))
    user_id = db.Column(db.Integer(), db.ForeignKey('user_data.id'))
    start_time = db.Column(db.DateTime, nullable=False)
    vehicle_no = db.Column(db.String(20),nullable=False)
    
    #when user will release the spot then it will stored
    end_time = db.Column(db.DateTime, nullable=True)
    parking_cost = db.Column(db.Float, nullable=True)
