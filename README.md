
# Vehicle-Parking-App Project
### Author

Chhotu Kumar  
[chhotu_kumar@zohomail.in](mailto:chhotu_kumar@zohomail.in)  
I believe in the power of hard work to drive success, challenges with relentless dedication and turning persistent effort into innovative technological solutions that make a real impact.

This is my _MAD1 Project_, problem statement on vehicle_parking_web_application.

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
        parking_cost.html
        register.html
        registered_users.html
        reserve_spot.html
        spot.html
        summary.html
```

![Model image.](/static/images/model_img.png "This is a model image.")

