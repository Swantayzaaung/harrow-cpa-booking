import os
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_ngrok import run_with_ngrok 
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
from forms import LoginForm, RegisterForm, BookingForm
from flask_login import LoginManager, current_user, login_user, logout_user

ROOMS = ['A101','A102','A103','A104','A105','A106','A107','A108','A109','A110',
         'A201','A202','A203','A204','A205','A206','A207','A208','A209','A220']


basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "swanisacutiepatootie"

run_with_ngrok(app)

db = SQLAlchemy(app)
login_manager = LoginManager(app)

from models import User, Bookings

@app.route("/", methods=["GET", "POST"])
def index():
    available_rooms = ROOMS
    # Do some logic to display the available rooms
    return render_template("index.html", rooms=available_rooms, title="Home")


@app.route('/register', methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("index"))

    form = RegisterForm()
    
    if form.validate_on_submit(): # if the register form has been submitted
        
        username = form.username.data
        email = form.email.data
        password = form.password.data
        year = form.year.data
        house = form.house.data
        tutor_group = house + str(year) 
        print(tutor_group)
        
        # hash email and password
        password_hash = generate_password_hash(password)

        # adding user to the database
        new_user = User(email=email, username=username, password=password_hash, tutor_group=tutor_group)

        db.session.add(new_user)
        db.session.commit()

        flash("Account created. Please login with your credentials.", 'success')
        return redirect(url_for('login'))

    return render_template("register.html", title="Sign Up", form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    form = LoginForm()

    if form.validate_on_submit(): # if the login form has been submitted
        # checking if there is a record with the email that is inputted, will return a User object if there is. Will return None if there is no record with that email
        user = User.query.filter_by(email=form.email.data).first()

        # do verification checks here
        if user and check_password_hash(user.password, form.password.data): # change the bcrypt stuff to your hash module thing
            login_user(user)
            return redirect(url_for('index'))
        else:
            flash('Your email or password is incorrect.', 'danger')
        print("login")
    return render_template("login.html", title="Login", form=form)

@app.route("/logout")
def logout():
    logout_user()
    # Redirect user to login form
    return redirect(url_for("index"))

@app.route('/layoutt')
def layoutt():
    return render_template("layout.html")

@app.route('/book', methods=["POST"])
def book():
    if request.method == "POST" and current_user.is_authenticated: 
        room_id = request.form.get("room_id")
        num_people = request.form.get("num_people")
        timeslot = request.form.get("timeslot")
        date = request.form.get("date")
        booking_records = Bookings.query.filter_by(rid=room_id, date=date, time_slot=timeslot).all()
        if not booking_records:
            booking = Bookings(rid=room_id, uid=current_user.id, date=date, num_people=num_people, time_slot=timeslot)
            db.session.add(booking) 
            db.session.commit()
        else:
            pass
            # send a message to user saying there is a booking already
    return redirect(url_for("index"))
        


# Run the flask server on the local network
# Run the flask server on the local network
# Run the flask server on the local network
if __name__ == '__main__':
    app.run(debug=True)
