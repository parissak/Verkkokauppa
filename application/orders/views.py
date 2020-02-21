from flask import redirect, render_template, request, url_for, flash
from flask_login import current_user, login_required

from application import app, db
from application.products.models import Product
from application.categories.models import Category
from application.orders.models import Order

from application.products.forms import ProductForm
from application.products.forms import SearchForm

from sqlalchemy.sql import text
 
# post new order
@app.route("/order", methods=["GET", "POST"])
@login_required
def order_new():

    product_id = request.form.get("id")
    user = current_user

    order = Order()
    order.account_id = user.id
    order.product_id = product_id
 
    db.session().add(order)
    db.session().commit()    

    flash("Item ordered succesfully", "successful")
     
    return redirect(url_for("products_index"))
    
