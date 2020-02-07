from application import db
from application.models import Base

from sqlalchemy.sql import text

class Category(Base):
    name = db.Column(db.String(30), nullable=False)
    products = db.relationship("Product", backref='category', lazy=True)


@staticmethod
def return_id(category_name):    
    stmt = text("SELECT * FROM Category" 
    " WHERE name = :x").params(x = category_name)
       
    res = db.engine.execute(stmt).fetchone()

    id = res[0]
    return id

# INSERT INTO Category (id, name) VALUES (1, 'Electronics');
# INSERT INTO Category (id, name) VALUES (2, 'Clothes');
# INSERT INTO Category (id, name) VALUES (3, 'Home & Garden');
