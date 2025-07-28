
# Vehicle-Parking-App
<!-- it is vehicle parking web app developed using python framework "Flask". -->
## Overview
It is a `Vehicle-Parking-App` a web application developed using the Python framework __flask__.

## Technologies used

- **flask:** flask is a python framework for web development,it is used for handling routing, sessions, and server logic.
- **flask_sqlalchemy:** flask_sqlalchemy is a object relational mapper(orm). It is a flask extention.
- **jinja2:** jinja 2 is a templating engine, it is used to render dynamic HTML content in web applications.
- **bootstrap:** it is a pre-written frontend code, it is used for responsive interface.
- **matplotlib:** it is a plotting library in python, it is used for generating graphs for data visualisation.


## Key Features
- **Authentication:** Secured login for admin and user
- **Admin Dashboard:** The admin can _create/edit/delete_ a parking lot, admin can _view the status_ of parking spot and check the parked vehicle details If the parking spot status is occupied and admin can view _all registered users_.
- **User Dashboard:** The user can choose an available parking lot and once user release the spot parking cost will display.
- **Summary Graph:** For data visualisation, graphs are there for both user and admin. 

## Folder Structure
```
C:.
│   .gitignore
│   app.py
│   README.md
│   requirements.txt
│
├───controller
│   │   all_routes.py
│   │   models.py
│   │
│   └───__pycache__
│           all_routes.cpython-313.pyc
│           models.cpython-313.pyc
│
├───instance
│       project.db
│
├───static
│   │   style.css
│   │   summary1.png
│   │   usersummaryhist1.png
│   │   usersummaryhist2.png
│   │
│   └───images
│           image1.jpg
│           image2.jpg
│           image3.jpg
│           image4.jpg
│
└───templates
        add_lot.html
        admin_dashboard.html
        base.html
        dashboard.html
        edit_lot.html
        index.html
        login.html
        nav.html
        register.html
        registered_users.html
        reserve_spot.html
        spot.html
        summary.html
```
## Models
- **UserData:** It stores user _information(or data)_, user role and stores authentication data.
- **ParkingLot:** It stores data of about parking lots.
- **ParkingSpot:** It stores data of about parking spots status.
- **ReservedSpot:** It stores data of users who has reserved _a spot or spots_ also stores vehicle data, reservation timings and parking cost.

![Model image.](/static/images/model_img.png "This is a model image.")

