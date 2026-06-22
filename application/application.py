print("aaaaaa開始")
from dotenv import load_dotenv
import os
from flask import Flask, render_template, request, redirect, session, url_for
from flask_caching import Cache
# from config import TEMPLATES_PATH, TEXT_PATH
from werkzeug.security import generate_password_hash, check_password_hash
from application.models import db, User, GroupBuy, Order
# from flask_sqlalchemy import SQLAlchemy
from application.helpers import *

# app = Flask(__name__, template_folder=TEMPLATES_PATH)

load_dotenv()
app = Flask(__name__)
# app.secret_key = "groupbuy_secret"
# app.config[
#     'SQLALCHEMY_DATABASE_URI'
# ] = 'sqlite:///groupbuy.db'

app.config[
    'SQLALCHEMY_DATABASE_URI'
] = os.environ["DATABASE_URL"]

app.config[
    "SQLALCHEMY_TRACK_MODIFICATIONS"
] = False

app.config["CACHE_TYPE"] = "simple"
app.config["CACHE_DEFAULT_TIMEOUT"] = 3600
cache = Cache(app)

# db = SQLAlchemy()
db.init_app(app)

app.secret_key = os.environ["SECRET_KEY"]


@app.route("/")
def home():
    groupbuys = GroupBuy.query.all()
    return render_template("home.html", groupbuys=groupbuys)

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        existing_user = User.query.filter(
            (
                User.username == username
            ) |
            (
                User.email == email
            )
        ).first()

        if existing_user:

            return "帳號或 Email 已存在"

        hashed_password = (
            generate_password_hash(
                password
            )
        )

        user = User(
            username=username,
            email=email,
            password_hash=hashed_password
        )

        db.session.add(user)
        db.session.commit()

        return redirect("/login")

    return render_template(
        "register.html"
    )

@app.route("/login", methods=["GET", "POST"])
# @cache.cached()
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        user = User.query.filter_by(
            email=email
        ).first()

        if not user:

            return "找不到帳號"

        if not check_password_hash(
            user.password_hash,
            password
        ):
            return "密碼錯誤"

        session["user_id"] = user.id
        session["username"] = user.username

        return redirect(
            url_for("home")
        )

    return render_template(
        "login.html"
    )

# @app.route("/dashboard")
# def dashboard():

#     if "user_id" not in session:

#         return redirect("/login")

#     return render_template(
#         "dashboard.html",
#         username=session["username"]
#     )

@app.route("/create-groupbuy", methods=["GET", "POST"])
def create_groupbuy():
    if "user_id" not in session:
        return redirect(url_for("login"))
    
    if request.method == "POST":
        add_groupbuy(    
            request.form["title"],
            request.form["image_url"],
            request.form["description"],
            request.form["product_url"],
            request.form["deadline"],
            request.form["delivery_method"],
            session["user_id"]
        )
        return redirect(url_for("home"))
    return render_template("create_groupbuy.html")

@app.route("/logout")
def logout():

    session.clear()

    return redirect("/")


# @cache.cached()
# @app.route("/organizer/login")
# def organizer_login():
#     return render_template(
#         "organizer_login.html"
#     )


# @app.route("/consumer/login")
# def consumer_login():
#     return render_template(
#         "consumer_login.html"
#     )


# @app.route("/organizer/dashboard")
# def organizer_dashboard():
#     return render_template(
#         "organizer_dashboard.html"
#     )


# @app.route("/consumer/dashboard")
# def consumer_dashboard():
#     return render_template(
#         "consumer_dashboard.html"
#     )


if __name__ == "__main__":
    app.run(debug=True)