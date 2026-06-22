from application.application import app
from application.models import db, User, GroupBuy, Order

with app.app_context():

    data = [
        GroupBuy(
            title="星巴克咖啡團",
            image_url="https://cielor.store/cdn/shop/files/PassportBlack.png?v=1779843105&width=400",
            description="一起買咖啡比較便宜",
            deadline="剩餘3天",
            organizer_id=1,
            participants=12,
            delivery_method="送貨到府"
        ),

        GroupBuy(
            title="Costco 零食團",
            image_url="https://cielor.store/cdn/shop/files/1778604937452.png?v=1778605277&width=400",
            description="代購Costco零食",
            deadline="剩餘5天",
            organizer_id=1,
            participants=18,
            delivery_method="送貨到府"
        ),

        GroupBuy(
            title="麥當勞早餐團",
            image_url="https://cielor.store/products/clr-monogram-hoodie-duplicate-duplicate",
            description="明天早餐一起訂",
            deadline="剩餘1天",
            organizer_id=1,
            participants=7,
            delivery_method="送貨到府"
        )
    ]

    db.session.add_all(data)
    db.session.commit()

    print("測試資料建立完成")