from application import db
from application.models import Base

from sqlalchemy.sql import text
from sqlalchemy import event

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    products = db.relationship("Product", backref='category', lazy=True)

@staticmethod
def return_id(category_name):    
    stmt = text("SELECT * FROM Category" 
    " WHERE name = :x").params(x = category_name)
       
    res = db.engine.execute(stmt).fetchone()

    id = res[0]
    return id

@event.listens_for(Category.__table__, 'after_create')
def insert_initial_values(*args, **kwargs):
    db.session.add(Category(name='Electronics'))
    db.session.add(Category(name='Clothes'))
    db.session.add(Category(name='Home & Garden'))
    db.session.commit()