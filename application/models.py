print("models.py 開始")
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Enum

db = SQLAlchemy()

class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    username = db.Column(
        db.String(50),
        nullable=False,
        unique=True
    )

    email = db.Column(
        db.String(100),
        nullable=False,
        unique=True
    )

    password_hash = db.Column(
        db.String(255),
        nullable=False
    )

    phone = db.Column(
        db.String(20),
        nullable=False,
    )

    plan = db.Column(
        Enum(
            "free",
            "pro",
            "business",
            name="plan_type"
        ),
        nullable=False,
        default="free"
    )

class GroupBuy(db.Model):

    __tablename__ = "groupbuys"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    title = db.Column(
        db.String(100),
        nullable=False
    )

    image_url = db.Column(
        db.String(500)
    )

    product_url = db.Column(
        db.String(500)
    )

    description = db.Column(
        db.Text
    )

    deadline = db.Column(
        db.String(50)
    )

    organizer_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    participants = db.Column(
        db.Integer,
        default=0
    )

    delivery_method = db.Column(
        db.String(50)
    )

    status = db.Column(
        db.String(20),
        default="open"
    )

class Order(db.Model):

    __tablename__ = "orders"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    quantity = db.Column(
        db.Integer,
        nullable=False
    )

    remark = db.Column(
        db.String(255)
    )

    # delivery_info = db.Column(
    #     db.String(255)
    # )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    groupbuy_id = db.Column(
        db.Integer,
        db.ForeignKey("groupbuys.id"),
        nullable=False
    )

    user = db.relationship(
        "User",
        backref="orders"
    )

    groupbuy = db.relationship(
        "GroupBuy",
        backref="orders"
    )
