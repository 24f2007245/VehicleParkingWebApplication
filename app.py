from flask import Flask,render_template, request

from controller.models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] ='this_is_my_secret_key'

db.init_app(app)

def create_tables():
    with app.app_context():
        db.create_all()
        admin = UserData.query.filter_by(roles='admin').first()
        if not admin:
            admin = UserData(
                user_name = 'admin',
                user_email = 'admin@admin.com',
                password = 'admin',
                roles = 'admin' 
            )
            db.session.add(admin)
            db.session.commit()

# class User(db.Model):
#     email = db.Column(db.String(120), unique=True, nullable=False, primary_key=True)
#     password = db.Column(db.String(200), nullable=False)
from controller.all_routes import *
if __name__ == '__main__':
    create_tables()
    app.run(debug=True) 