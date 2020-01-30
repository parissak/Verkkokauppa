from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.products.models import Product
from application.products.forms import ProductForm

# list
@app.route("/products", methods=["GET"])
def products_index():
    return render_template("products/list.html", products = Product.query.all())

# new
@app.route("/products/new/")
def products_form():
    return render_template("products/new.html", form = ProductForm())

# delete
@app.route("/products/<product_id>/", methods=["POST"])
def products_delete(product_id):
    product = Product.query.get(product_id)
    db.session.delete(product)
    db.session().commit()
  
    return redirect(url_for("products_index"))

# change description
@app.route("/products/<product_id>/", methods=["POST"])
def products_set_description(product_id):

    product = Product.query.get(product_id)
    newValue = request.form.get("newdesc")
    
    if newValue:
        product.description = newValue
        db.session().commit()
  
    return redirect(url_for("products_index"))

# post product
@app.route("/products/", methods=["POST"])
def products_create():
    form = ProductForm(request.form)

    if not form.validate():
        return render_template("products/new.html", form = form)

    product = Product(form.name.data, form.price.data, 
    form.description.data)
    product.account_id = current_user.id

    db.session().add(product)
    db.session().commit()

    return redirect(url_for("products_index"))
