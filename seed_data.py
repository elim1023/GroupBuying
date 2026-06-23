from application.application import app
from application.models import db, User, GroupBuy, Order
from werkzeug.security import generate_password_hash
from datetime import date

with app.app_context():

    data = [
        User(
            username = "Chopper",
            email = "Chopper@gmail.com",
            password_hash = generate_password_hash("Chopper"),
            phone = "0123456789",
            plan = "business"
        ),

        GroupBuy(
            title="星巴克咖啡團",
            image_url="https://www.starbucks.com.tw/common/objects/images/product/2026051809574854_24.jpg",
            description="一起買咖啡比較便宜",
            price=120,
            deadline=date(2026, 6, 30),
            organizer_id=1,
            participants=12,
            delivery_method="送貨到府"
        ),

        GroupBuy(
            title="Costco 零食團",
            image_url="https://www.costco.com.tw/medias/sys_master/images/hb2/h0a/312933354536990.jpg",
            description="代購Costco零食",
            price=100,
            # deadline="剩餘5天",
            deadline=date(2026, 7, 10),
            organizer_id=1,
            participants=18,
            delivery_method="送貨到府"
        ),

        GroupBuy(
            title="Basic Passport Holder (Black)",
            image_url="https://cielor.store/cdn/shop/files/PassportBlack.png?v=1779843105&width=400",
            description="錢包",
            price=1400,
            # deadline="剩餘12天",
            deadline=date(2026, 7, 18),
            organizer_id=1,
            participants=26,
            delivery_method="送貨到府"
        ),

        GroupBuy(
            title="Cielor Premium Tumbler (Black)",
            image_url="https://cielor.store/cdn/shop/files/1778604937452.png?v=1778605277&width=400",
            description="明天早餐一起訂",
            price=1500,
            # deadline="剩餘20天",
            deadline=date(2026, 8, 10),
            organizer_id=1,
            participants=46,
            delivery_method="送貨到府"
        ),

        GroupBuy(
            title="亞尼克生乳捲, 三顆布丁",
            image_url="https://photo.yannick.com.tw/photo/0101357/1.jpg",
            description="布丁",
            price=150,
            # deadline="剩餘10天",
            deadline=date(2026, 7, 6),
            organizer_id=1,
            participants=100,
            delivery_method="送貨到府"
        ),

    ]

    db.session.add_all(data)
    db.session.commit()

    print("測試資料建立完成")