from flask import  render_template, flash, redirect, url_for, request
from flask_login import LoginManager, UserMixin, login_user
from .database.models import db, User
from webapp import app



login_manager = LoginManager()
login_manager.init_app(app)

# Create a User class that inherits from UserMixin
class User(UserMixin):
    def __init__(self, username, password):
        self.username = username
        self.password = password

@login_manager.user_loader
def load_user(user_id):
    # Retrieve the user from the database based on the user_id
    return User.query.get(user_id)

@app.route("/")
@app.route("/Home")
def index():
    trend_novels = ["Trend Novel 1", "Trend Novel 2", "Trend Novel 3"]
    fanfic_books = ["Fanfic Book 1", "Fanfic Book 2", "Fanfic Book 3"]
    fanfic_tags = ["Tag 1", "Tag 2", "Tag 3"]
    ranked_novels = ["Ranked Novel 1", "Ranked Novel 2", "Ranked Novel 3"]
    potential_starlets = ["Starlet Novel 1", "Starlet Novel 2", "Starlet Novel 3"]
    rising_fanfictions = ["Rising Fanfiction 1", "Rising Fanfiction 2", "Rising Fanfiction 3"]
    completed_novels = ["Completed Novel 1", "Completed Novel 2", "Completed Novel 3"]
    recommendations = ["Recommendation 1", "Recommendation 2", "Recommendation 3"]
    
    return render_template("index.html", index=True, trend_novels=trend_novels, fanfic_books=fanfic_books, fanfic_tags=fanfic_tags,
                           ranked_novels=ranked_novels, potential_starlets=potential_starlets,
                           rising_fanfictions=rising_fanfictions, completed_novels=completed_novels,
                           recommendations=recommendations)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user, remember=True)
            flash("Login successful!", "success")
            return redirect(url_for("dashboard"))
        else:
            flash("Invalid username or password", "error")
            return redirect(url_for("login"))
    
    return render_template("login.html", login=True)

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        # Extract form data
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")

        # Check if username or email already exists
        if User.query.filter_by(username=username).first():
            flash("Username already exists", "error")
        elif User.query.filter_by(email=email).first():
            flash("Email already exists", "error")
        elif password != confirm_password:
            flash("Passwords do not match", "error")
        else:
            # Create a new user
            user = User(username=username, email=email)
            user.set_password(password)
            db.session.add(user)
            db.session.commit()

            flash("Registration successful! You can now log in.", "success")
            return redirect(url_for("login"))

    return render_template("signup.html", signup=True)

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html", dashboard=True)

@app.route("/latest")
def latest():
    return render_template("latest.html", latest=True)
