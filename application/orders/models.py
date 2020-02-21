from application import db
from application.models import Base

class Order(Base):
    shipped = db.Column(db.Boolean, nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable = False)

    def __init__(self):
        self.shipped = False