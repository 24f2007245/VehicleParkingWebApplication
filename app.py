from flask import Flask,render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
db = SQLAlchemy()
db.init_app(app)

def create_tables():
    with app.app_context():
        db.create_all()

class User(db.Model):
    # __tablename__ = 'userInMyApplicaiton'
    email = db.Column(db.String(120), unique=True, nullable=False, primary_key=True)
    password = db.Column(db.String(200), nullable=False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        user_email = request.form['user_email']
        password = request.form['password']

        user= User.query.filter_by(email=user_email).first()
        
        if user_email == user.email and password == user.password:
            return render_template('dashboard.html', user_email=user.email)
        else:
            print(f"Login attempt with email: {user_email} and password: {password}")
            return render_template('login.html', error='Invalid credentials')
   

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user_email= request.form['user_email']
        password = request.form['password']
        db.session.add(User(email=user_email, password=password))
        db.session.commit()
        # Here you would typically save the new user to a database
        return render_template('login.html', success='Registration successful, please log in.')
    return render_template('register.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
    create_tables()
    app.run(debug=True) 