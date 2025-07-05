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

        if 'admin' in user.roles:
            return render_template('admin_dashboard.html')
        
        flash('login successful', 'success')
        return render_template('dashboard.html')
   

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user_name= request.form.get('user_name')
        user_email= request.form.get('user_email')
        password = request.form.get('password')
        vehicle_no = request.form.get('vehicle_no')
        address = request.form.get('Address')
        if UserData.query.filter_by(user_email=user_email).first():
            flash('Email already registered.', 'error')
            return redirect(url_for('register'))
        db.session.add(UserData(user_name=user_name, user_email=user_email, password=password,vehicle_no=vehicle_no, address=address))
        db.session.commit()
        
        return render_template('login.html', success='Registration successful, please log in.')
    return render_template('register.html')

@app.route('/dashboard')
def dashboard():
    if 'email' not in session:
        flash('Please login to access the dashboard.', 'warning')
        return redirect(url_for('login'))
    
    if 'roles' in session and 'admin' in session['roles']:
        return render_template('admin_dashboard.html')
    
    return render_template('dashboard.html')

@app.route('/registered_users')
def registered_users():
    return render_template('registered_users.html',usersdata=UserData.query.all())

@app.route('/add_lot', methods=['GET', 'POST'])
def add_lot():
    if request.method == 'POST':
        id = request.form.get('id')
        location = request.form.get('location')
        total_slots = request.form.get('total_slots')
        pin_code = request.form.get('pin_code')
        price = request.form.get('price')
        address = request.form.get('address')

        # Convert data types (important!)
        try:
            total_slots = int(total_slots) if total_slots else 0
            price = float(price) if price else 0.0
        except ValueError:
            flash("Invalid input for slots or price", "error")
            return redirect(url_for('add_lot'))

        if ParkingLot.query.filter_by(id=id).first():
            flash('Parking lot already exists.', 'error')
            return redirect(url_for('add_lot'))

        new_lot = ParkingLot(id=id, location=location, total_slots=total_slots,
                             pin_code=pin_code, price=price, address=address)
        db.session.add(new_lot)
        db.session.commit()

        flash('Parking lot added successfully.', 'success')
        return redirect(url_for('add_lot'))  # Or redirect to another page
    return render_template('add_lot.html')

@app.route('/go_add_lot')
def go_add_lot():
    return render_template('add_lot.html')

@app.route('/logout')
def logout():
    session.pop('email', None)
    session.pop('roles', None)
    flash('You have been logged out.', 'success')
    return redirect(url_for('login'))
