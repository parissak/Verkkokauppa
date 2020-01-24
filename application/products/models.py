from application import db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    name = db.Column(db.String(144), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(144), nullable=False)

    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description
