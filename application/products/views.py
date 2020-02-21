from flask import redirect, render_template, request, url_for
from flask_login import current_user, login_required

from application import app, db
from application.products.models import Product
from application.categories.models import Category

from application.products.forms import ProductForm
from application.products.forms import SearchForm

from sqlalchemy.sql import text
 
# list & search
@app.route("/products", methods=["GET", "POST"])
def products_index():
    if request.method == 'POST':
        form = SearchForm(request.form)
        product_name = request.form.get("search")

        if not product_name:
            result = Product.query.all()
        else:
            result = Product.query.filter_by(name=product_name).all() 

    if request.method == 'GET':
        result = Product.query.all()
     
    return render_template("products/list.html", form = SearchForm(), products = result)
    
# new
@app.route("/products/new/")
@login_required
def products_form():
    return render_template("products/new.html", form = ProductForm(), categories = Category.query.all())

# delete product
@app.route("/products/delete/<product_id>", methods=["POST"])
@login_required
def products_delete(product_id):
    product = Product.query.get(product_id)
    db.session.delete(product)
    db.session().commit()
  
    return redirect(url_for("auth_user"))

# change description
@app.route("/products/change/<product_id>", methods=["POST"])
@login_required
def products_set_description(product_id):

    product = Product.query.get(product_id)
    new = request.form.get("newdesc")
    
    if new:
        product.description = new
        db.session().commit()
  
    return redirect(url_for("auth_user"))

# post product
@app.route("/products/", methods=["POST"])
@login_required
def products_create():
    form = ProductForm(request.form)

    if not form.validate():
        return render_template("products/new.html", form = form)

    # selection from form & dropdown list
    category_name = request.form.get("select")

    # get id from name query 
    stmt = text("SELECT * FROM Category" 
    " WHERE name = :x").params(x = category_name)   
    res = db.engine.execute(stmt).fetchone()
    category_id = res[0]

    product = Product(form.name.data, form.price.data, 
    form.description.data)
    product.account_id = current_user.id
    product.category_id = category_id

    db.session().add(product)
    db.session().commit()

    print("Logging message", flush=True)

    return redirect(url_for("auth_user"))
