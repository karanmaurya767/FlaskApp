from flask import Flask, render_template, request, redirect, url_for, session,flash
from config import Config
from extensions import db
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config.from_object(Config)

# SQLAlchemy को app से जोड़ो
db.init_app(app)

# Models import करो
from models import User








@app.route("/")
def home():
    return render_template("index.html")

@app.route("/dashboard")
def dashboard():
    
    if "user_id" not in session:
        flash("you are currenly log out" , "danger")
        return  redirect(url_for("login"))

    return render_template("dashboard.html", name = session["user_name"])

@app.route("/register", methods = ["GET", "POST"])
def register():

    if request.method =="POST":

        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        hashed_password  = generate_password_hash(password)

        if not all([name,email, password]):
            flask("All fields are required.", "danger")
            return redirect(url_for("register"))

        existing_user = User.query.filter_by(email=email).first()

        if existing_user:
            flash("Email already exists.", "warning")
            return redirect(url_for("register"))

        user = User(
            name = name , 
            email = email, 
            password = hashed_password
        )

        db.session.add(user)
        db.session.commit()

        flash("Registration Successful. Please Login.", "success")
        return redirect(url_for("login"))

    return render_template("registration.html")

@app.route("/login", methods = ["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        user = User.query.filter_by(email = email).first()


        if user and check_password_hash(user.password, password):
            session["user_id"] = user.id
            session["user_name"] = user.name
            flash("welcome Back...", "success")
            return redirect(url_for("dashboard"))
        flash(" Invalid Email or Password", "danger")
        return redirect(url_for("login"))

    return render_template("login.html")

@app.route("/logout")
def logout():

    session.clear()
    flash("You are log out now", "success")
    return redirect(url_for("home"))








with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)