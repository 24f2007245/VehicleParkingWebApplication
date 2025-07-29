
# Vehicle-Parking-App Project
### Author

Chhotu Kumar  
24f2007245  
[24f2007245@ds.study.iitm.ac.in](mailto:24f2007245@ds.study.iitm.ac.in)  
I believe in the power of hard work to drive success, tackling challenges with relentless dedication and turning persistent effort into innovative technological solutions that make a real impact.
It is a `Vehicle-Parking-App` a web application developed using the Python framework __flask__.

### Overview

It is a multi-user app (one requires an administrator and other users) that manages different parking lots, parking spots,  parked vehicles and data visualization using graphs. The aim is to build a responsive, secure system that deals with live parking status and cost calculations.

### Technologies used

- **flask:** flask is a python framework for web development,it is used for handling routing, sessions, and server logic.
- **flask_sqlalchemy:** flask_sqlalchemy is a object relational mapper(orm). It is a flask extention.
- **sqlite:** database engine used for storing data.
- **jinja2:** jinja 2 is a templating engine, it is used to render dynamic HTML content in web applications.
- **bootstrap:** it is a pre-written frontend code, it is used for responsive interface.
- **matplotlib:** it is a plotting library in python, it is used for generating graphs for data visualisation.


### Architecture and Key Features
#### Architecture Details-

* Platform: Web-based  
* Architecture: Client-server  
* Software architecture/Design Pattern: Model-View-Controller(MVC)

#### Key Features-
- **Authentication:** Secured login for admin and user
- **Admin Dashboard:** The admin can _create/edit/delete_ a parking lot, admin can _view the status_ of parking spot and check the parked vehicle details If the parking spot status is occupied and admin can view _all registered users_.
- **User Dashboard:** The user can choose an available parking lot and once user release the spot parking cost will display.
- **Summary Graph:** For data visualisation, graphs are there for both user and admin. 

### Folder Structure
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
### DB Schema Design

The database uses SQLite via Flask-SQLAlchemy:

* UserData: Columns \- id (Integer, Primary Key, Autoincrement), user\_name (String, Not Null),user\_email (String, Not Null, Unique),password (String, Not Null),address (String, Nullable), role (String, default 'user'). A one-to-many relationship with the reserved\_spot.  
* ParkingLot: Columns \- id (Integer, Primary Key, Autoincrement), lot\_name (String, Not Null), pin\_code(Integer, Not null), price(Integer, Not Null), address (String, Not Null), total\_spots (Integer, Not null), reserved\_spots(Integer, default 0). A one-to-many relationship with the parking\_spot table.  
* ParkingSpot: Columns \- id (Integer, Primary Key, Autoincrement), lot\_id (Integer, Foreign Key to parking\_lot.id), status (String, default 0/available). A one-to-many relationship with the reserved\_spot.  
* ReservedSpot: Columns \- id (Integer, Primary Key, Autoincrement), user\_id (Integer, Foreign Key to user\_data), spot\_id (Integer, Foreign Key to parking\_spot.id), vehicle\_no (String, Not Null), start\_time (DateTime, Not Null), end\_time (DateTime, Not Null), parking\_cost (Float, not Null). 

Reasons behind designing this way- Primary keys and unique emails maintain user integrity. Foreign keys ensure that reservations and spots point to valid lots and users. Spot status is managed with an availability flag.

![Model image.](/static/images/model_img.png "This is a model image.")

