from application import db
from application.models import Base

from sqlalchemy.sql import text

class User(Base):

    __tablename__ = "account"
   
    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)

    products = db.relationship("Product", backref='account', lazy=True)

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
  
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    @staticmethod
    def count_items(users_id):
        stmt = text("SELECT COUNT(product.name) FROM Account" 
        " JOIN product on account.id = account_id WHERE" 
        " Account.id = :x").params(x = users_id)

        res = db.engine.execute(stmt).fetchone()

        item_count = res[0]
        return item_count