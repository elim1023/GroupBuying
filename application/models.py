print("models.py 開始")
from flask_sqlalchemy import SQLAlchemy

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


# print("models.py 開始")

# from flask_sqlalchemy import SQLAlchemy

# print("SQLAlchemy import 完成")

# db = SQLAlchemy()

# print("db 建立完成")

# class User(db.Model):

#     print("User class 建立中")

#     __tablename__ = 'users'

#     id = db.Column(
#         db.Integer,
#         primary_key=True
#     )

#     username = db.Column(
#         db.String(50),
#         nullable=False,
#         unique=True
#     )

#     email = db.Column(
#         db.String(100),
#         nullable=False,
#         unique=True
#     )

#     password_hash = db.Column(
#         db.String(255),
#         nullable=False
#     )

# print("models.py 結束")