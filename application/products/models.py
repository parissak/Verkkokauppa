from application import db
from application.models import Base

class Product(Base):
    name = db.Column(db.String(144), nullable=False)
    price = db.Column(db.Float(2), nullable=False)
    description = db.Column(db.String(144), nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable = False)

    Order = db.relationship("Order", uselist=False, backref="Product")

    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description