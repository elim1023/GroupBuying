from application.application import app
from application.models import db


with app.app_context():

    db.create_all()

    print("資料庫建立完成")
