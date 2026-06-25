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

        User(
            username = "Mary",
            email = "Mary@gmail.com",
            password_hash = generate_password_hash("Mary"),
            phone = "123456789",
        ),

        User(
            username = "Freen",
            email = "Freen@gmail.com",
            password_hash = generate_password_hash("Freen"),
            phone = "0919980808",
        ),

        User(
            username = "Becky",
            email = "Becky@gmail.com",
            password_hash = generate_password_hash("Becky"),
            phone = "0920021205",
        ),

        User(
            username = "Tom",
            email = "Tom@gmail.com",
            password_hash = generate_password_hash("Tom"),
            phone = "0996378520",
            plan = "Pro",
        ),

        User(
            username = "Sam",
            email = "Sam@gmail.com",
            password_hash = generate_password_hash("Sam"),
            phone = "0959634870",
            plan = "business",
        ),

        User(
            username = "Sky",
            email = "Sky@gmail.com",
            password_hash = generate_password_hash("Sky"),
            phone = "0920378520",
        ),

        GroupBuy(
            title="亞尼克 三顆布丁生乳捲",
            image_url="https://photo.yannick.com.tw/photo/0101357/1.jpg",
            description="布丁",
            price=360,
            deadline=date(2026, 7, 6),
            organizer_id=1,
            participants=19,
            delivery_method="送貨到府"
        ),

        GroupBuy(
            title="Costco 零食團-翠果子櫻花米果禮盒",
            image_url="https://www.costco.com.tw/medias/sys_master/images/hb2/h0a/312933354536990.jpg",
            description="Costco零食代購\n1盒 X 14公克 X 20包",
            price=100,
            deadline=date(2026, 7, 10),
            organizer_id=5,
            participants=0,
            delivery_method="送貨到府"
        ),

        GroupBuy(
            title="Buonissimo 柏尼西蒙-瑪沙拉酒風味提拉米蘇-大盒",
            image_url="https://cdn-general.cybassets.com/media/W1siZiIsIjM1MDA5L3Byb2R1Y3RzLzYzNjQwNDUwLzE3NjYxNTI1ODJfNzNjMzA5NzE5NjZkMmVhZTE2MzYucG5nIl0sWyJwIiwidGh1bWIiLCI2MDB4NjAwIl1d.png?sha=6a5dfbe41a71f0b3",
            description="團購滿1萬95折\n團購滿2萬9折\n團購滿3萬88折\n團購滿4萬85折",
            # https://www.buonissimo.com.tw/products/%E7%91%AA%E6%B2%99%E6%8B%89%E9%85%92%E9%A2%A8%E5%91%B3%E6%8F%90%E6%8B%89%E7%B1%B3%E8%98%87-%E5%A4%A7%E7%9B%92\n
            price=839,
            deadline=date(2026, 8, 16),
            organizer_id=1,
            participants=0,
            delivery_method="送貨到府"
        ),

        GroupBuy(
            title="【金黃起司乳酪條10入】-Celebrate 慶祝甜點工作室",
            image_url="https://myship.7-11.com.tw/i/cgdm/GM2112120993593/2112120048519488.jpg",
            description="冷凍可保存2週、冷藏可保存4天",
            price=500,
            deadline=date(2026, 8, 2),
            organizer_id=1,
            participants=52,
            delivery_method="送貨到府"
        ),

        GroupBuy(
            title="手搖飲蛋捲-玫瑰荔枝",
            image_url="https://www.cysweet.com.tw/upload/shop_b/thumb_351e6e3f0116745b5e201c2956d76dfd.jpg",
            description="原產地：台灣",
            price=240,
            deadline=date(2026, 8, 23),
            organizer_id=5,
            participants=150,
            delivery_method="超商取貨"
        ),

        GroupBuy(
            title="【MEOW】喵圈圈烤甜甜圈-卡士達甜甜圈 丹麥甜甜圈",
            image_url="https://myship.7-11.com.tw/i/cgdm/GM2404054069411/2606131213492432.jpg",
            description="",
            price=50,
            deadline=date(2026, 7, 15),
            organizer_id=6,
            participants=15,
            delivery_method="超商取貨"
        ),

        GroupBuy(
            title="鱈魚風味章魚燒片",
            image_url="https://www.dl-food.com/wp-content/uploads/UO1-768x768.png",
            description="",
            price=49,
            deadline=date(2026, 7, 30),
            organizer_id=5,
            participants=29,
            delivery_method="超商取貨"
        ),

        GroupBuy(
            title="OREO蔓越莓千層磚",
            image_url="https://yipinsiang.com.tw/shopping_goods_img/55/302.jpg",
            description="",
            price=115,
            deadline=date(2026, 8, 12),
            organizer_id=1,
            participants=129,
            delivery_method="超商取貨"
        ),

        GroupBuy(
            title="IN2IT 超柔滑粉餅SPF35 PA+++",
            image_url="https://pbs.twimg.com/media/HJKiYDgbUAAgXEI.jpg",
            description="",
            price=320,
            deadline=date(2026, 8, 8),
            organizer_id=3,
            participants=162,
            delivery_method="送貨到府"
        ),
        
        GroupBuy(
            title="認識台灣掛布",
            image_url="https://shoplineimg.com/6170c51fe70cc1004ad9d5e8/68f1ecb49c86a50010a3dba6/800x.webp?source_format=jpg",
            description="",
            price=480,
            deadline=date(2026, 7, 20),
            organizer_id=1,
            participants=20,
            delivery_method="送貨到府"
        ),

        GroupBuy(
            title="CLR Monogram Half- Zip (Black)",
            image_url="https://cielor.store/cdn/shop/files/quarter2.png?v=1779841248&width=1000",
            description="",
            price=2657,
            # deadline="剩餘12天",
            deadline=date(2026, 8, 12),
            organizer_id=4,
            participants=156,
            delivery_method="送貨到府"
        ),
    ]

    db.session.add_all(data)
    db.session.commit()

    print("測試資料建立完成")