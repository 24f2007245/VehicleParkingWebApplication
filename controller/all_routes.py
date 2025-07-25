from app import app

from flask import render_template, request, flash, redirect, url_for, session
from controller.models import *

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    
    if request.method == 'POST':
        email = request.form['user_email']
        password = request.form['password']

              # Fetch user from the database
        user= UserData.query.filter_by(user_email=email).first()
        

        if not user:
            flash('Email not registered.', 'error')
            return redirect(url_for('login'))
        
        
  
        if password != user.password:
            flash('Incorrect password.', 'danger')
            return redirect(url_for('login'))
        
        session['email'] = user.user_email
        session['roles'] = user.roles
        session['user_id']= user.id

        if 'admin' in user.roles:
            return redirect(url_for('dashboard'))
        
        flash('login successful', 'success')
        return redirect(url_for("dashboard"))
   

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user_name= request.form.get('user_name')
        user_email= request.form.get('user_email')
        password = request.form.get('password')
        address = request.form.get('Address')
        if UserData.query.filter_by(user_email=user_email).first():
            flash('Email already registered.', 'error')
            return redirect(url_for('register'))
        db.session.add(UserData(user_name=user_name, user_email=user_email, password=password, address=address))
        db.session.commit()
        
        return render_template('login.html', success='Registration successful, please log in.')
    return render_template('register.html')


@app.route('/dashboard')
def dashboard():
    if 'email' not in session:
        flash('Please login to access the dashboard.', 'warning')
        return redirect(url_for('login'))
    
    user_id = session['user_id']
    recent_reservations = ReservedSpot.query.filter_by(user_id=user_id).all()
    
    if 'roles' in session and 'admin' in session['roles']:
        return render_template('admin_dashboard.html',parking_lots=ParkingLot.query.all())
    return render_template('dashboard.html',lot=ParkingLot.query.all(),reserv=recent_reservations)


@app.route('/registered_users')
def registered_users():
    return render_template('registered_users.html',usersdata=UserData.query.all())


@app.route('/add_lot', methods=['GET', 'POST'])
def add_lot():
    if request.method == 'POST':
        id = request.form.get('id')
        lot_name = request.form.get('lot_name')
        total_spots = int(request.form.get('total_slots'))
        pin_code = request.form.get('pin_code')
        price = request.form.get('price')
        address = request.form.get('address')

        if ParkingLot.query.filter_by(id=id).first(): #checking for already exits or not
            flash('Parking lot already exists.', 'error')
            return redirect(url_for('add_lot'))

        new_lot = ParkingLot(id=id, lot_name=lot_name, total_spots=total_spots,pin_code=pin_code, price=price, address=address)
        db.session.add(new_lot)                         #adding new lot data
        db.session.commit()

        #creating all spots
        for i in range(1, total_spots+1):
            spot=ParkingSpot(lot_id=new_lot.id,status=0) #0-available
            db.session.add(spot)
        db.session.commit()

        flash('Parking lot added successfully.', 'success')
        return redirect(url_for('add_lot'))  
    return render_template('add_lot.html')


@app.route('/edit_lot/<int:id>', methods=['GET', 'POST'])
def edit_lot(id):
    lot = ParkingLot.query.get_or_404(id)

    if request.method == 'POST':
        lot.id = request.form.get('id') 
        lot.lot_name = request.form.get('lot_name')
        lot.address = request.form.get('address')
        lot.pin_code = request.form.get('pin_code')
        lot.total_spots = request.form.get('total_spots')
        lot.price = request.form.get('price')

        db.session.commit()

        return redirect(url_for('dashboard')) 

    return render_template('edit_lot.html', lot=lot)


@app.route('/logout')
def logout():
    session.pop('email', None)
    session.pop('roles', None)
    flash('You have been logged out.', 'success')
    return redirect(url_for('login'))


@app.route('/delete_lot/<int:id>')
def delete_lot(id):
    lot=ParkingLot.query.get_or_404(id)
    if lot.reserved_spots==0:
        db.session.delete(lot)
        db.session.commit()
        flash('Parking Lot Deleted, Successfully.','success')
    else:
        flash('There are reserved spot in this lot, unsuccessful','warning')
    return redirect(url_for('dashboard'))



#reservation related logics
@app.route('/reserve_spot/<int:id>', methods=['GET','POST'])
def reserve_spot(id):

    lot = ParkingLot.query.get_or_404(id)
    start_time = datetime.now()
    userid = session["user_id"]

    available_spot = ParkingSpot.query.filter_by(lot_id=lot.id, status=0).first()
    if not available_spot:
        flash("No available spot!", "warning")
        return redirect(url_for('dashboard'))

    
    if request.method == 'POST':
        vehicle_no=request.form.get('vehicle_no')
        new_reservation = ReservedSpot(spot_id=available_spot.id,user_id=userid,vehicle_no=vehicle_no,start_time=start_time)
        available_spot.status=1
        lot.reserved_spots += 1

        db.session.add(new_reservation) 

        db.session.commit()

        flash('Successfully! Your spot get reserved', 'success')
        return redirect(url_for('dashboard'))
    return render_template("reserve_spot.html",lot=lot,start_time=start_time)


@app.route('/release_spot/<int:id>', methods=['POST'])
def release_spot(id):
    reservation = ReservedSpot.query.get_or_404(id)
    spot = reservation.spot
    lot = spot.parking_lot
    
    end_time = datetime.now()
    duration_minutes = (end_time - reservation.start_time).total_seconds() / 60

    cost_per_minute = lot.price  
    total_cost = round(duration_minutes * cost_per_minute, 2)

    reservation.end_time = end_time
    reservation.parking_cost = total_cost
    spot.status = 0  #Making  Available again
    lot.reserved_spots -= 1

    db.session.commit()

    flash(f'Spot {spot.id} is released. Cost: ₹{total_cost}', 'success')
    return redirect(url_for('dashboard'))
