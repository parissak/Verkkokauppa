
from application import app, db
from flask import redirect, render_template, request, url_for
from application.products.models import Product

# list
@app.route("/products", methods=["GET"])
def products_index():
    return render_template("products/list.html", products = Product.query.all())

# new
@app.route("/products/new/")
def products_form():
    return render_template("products/new.html")

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
    product = Product(request.form.get("name"), 
    request.form.get("price"), 
    request.form.get("description"))
  
    db.session().add(product)
    db.session().commit()

    return redirect(url_for("products_index"))