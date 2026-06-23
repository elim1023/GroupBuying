print("aaaaaa開始")
from dotenv import load_dotenv
import os
from flask import Flask, render_template, request, redirect, session, url_for
from flask_caching import Cache
# from config import TEMPLATES_PATH, TEXT_PATH
from werkzeug.security import generate_password_hash, check_password_hash
from application.models import db, User, GroupBuy, Order
from application.helpers import *
from datetime import datetime

# app = Flask(__name__, template_folder=TEMPLATES_PATH)

load_dotenv()
app = Flask(__name__)

app.config[
    'SQLALCHEMY_DATABASE_URI'
] = 'sqlite:///groupbuy.db'

# app.config[
#     'SQLALCHEMY_DATABASE_URI'
# ] = os.environ["DATABASE_URL"]

app.config[
    "SQLALCHEMY_TRACK_MODIFICATIONS"
] = False

app.config["CACHE_TYPE"] = "simple"
app.config["CACHE_DEFAULT_TIMEOUT"] = 3600
cache = Cache(app)

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
        phone = request.form["phone"]

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
            password_hash=hashed_password,
            phone=phone
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

@app.route("/logout")
def logout():

    session.clear()

    return redirect("/")


@app.route("/create-groupbuy", methods=["GET", "POST"])
def create_groupbuy():
    if "user_id" not in session:
        return redirect(url_for("login"))
    
    if request.method == "POST":
        add_groupbuy(    
            request.form["title"],
            request.form["image_url"],
            request.form["product_url"],
            request.form["description"],
            request.form["price"],
            # request.form["deadline"],
            datetime.strptime(request.form["deadline"],"%Y-%m-%d").date(),
            request.form["delivery_method"],
            session["user_id"]
        )
        return redirect(url_for("home"))
    return render_template("create_groupbuy.html")

@app.route("/groupbuy/<int:groupbuy_id>", methods=["GET", "POST"])
def groupbuy_detail(groupbuy_id):

    groupbuy = GroupBuy.query.get_or_404(groupbuy_id)
    
    if request.method == "POST":

        if "user_id" not in session:
            return redirect(url_for("login"))
        
        order = Order(
            user_id=session["user_id"],
            groupbuy_id=groupbuy_id,
            quantity=int(request.form["quantity"]),
            remark=request.form["remark"],
            # delivery_info=request.form["delivery_info"]
        )

        db.session.add(order)

        groupbuy.participants += 1

        db.session.commit()

        return redirect(url_for("groupbuy_detail", groupbuy_id=groupbuy_id))

    return render_template("groupbuy_detail.html", groupbuy=groupbuy)

# 查看參與的團購
@app.route("/my-orders")
def my_orders():
    if "user_id" not in session:
        return redirect(url_for("login"))

    orders = Order.query.filter_by(user_id=session["user_id"]).all()

    return render_template("my_orders.html", orders=orders)

# 查看自己建立的團購
@app.route("/my-groupbuys")
def my_groupbuys():

    if "user_id" not in session:
        return redirect(url_for("login"))

    groupbuys = GroupBuy.query.filter_by(organizer_id=session["user_id"]).all()

    return render_template("my_groupbuys.html", groupbuys=groupbuys)

# 查看團購的跟團者
@app.route("/groupbuy/<int:groupbuy_id>/orders")
def groupbuy_orders(groupbuy_id):

    if "user_id" not in session:
        return redirect(url_for("login"))

    groupbuy = GroupBuy.query.get_or_404(groupbuy_id)

    # 防止別人查看你的團購
    if groupbuy.organizer_id != session["user_id"]:
        return redirect(url_for("home"))

    return render_template(
        "groupbuy_orders.html",
        groupbuy=groupbuy
    )

# 修改自己的訂單
@app.route("/order/<int:order_id>/edit", methods=["GET", "POST"])
def edit_order(order_id):

    if "user_id" not in session:
        return redirect(url_for("login"))

    order = Order.query.get_or_404(order_id)

    # 防止修改別人的訂單
    if order.user_id != session["user_id"]:
        return redirect(url_for("my_orders"))

    if request.method == "POST":

        order.quantity = int(request.form["quantity"])
        order.remark = request.form["remark"]
        order.delivery_info = request.form["delivery_info"]

        db.session.commit()

        return redirect(url_for("my_orders"))

    return render_template("edit_order.html", order=order)

# 刪除訂單
@app.route("/order/<int:order_id>/delete", methods=["POST"])
def delete_order(order_id):

    if "user_id" not in session:
        return redirect(url_for("login"))

    order = Order.query.get_or_404(order_id)

    if order.user_id != session["user_id"]:
        return redirect(url_for("my_orders"))

    db.session.delete(order)
    db.session.commit()

    return redirect(url_for("my_orders"))

@app.route("/pricing")
def pricing():
    return render_template("pricing.html")

# @cache.cached()

# @app.route("/organizer/dashboard")

# @app.route("/consumer/dashboard")


if __name__ == "__main__":
    app.run(debug=True)