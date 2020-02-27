from flask import redirect, render_template, request, url_for, flash
from flask_login import current_user, login_required
from application import app, db
from application.products.models import Product
from application.categories.models import Category
from application.orders.models import Order
from application.auth.models import User
from application.products.forms import ProductForm
from application.products.forms import SearchForm

 
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
@app.route("/products/delete/", methods=["POST"])
@login_required
def products_delete():
    id = request.form.get("delete_id")
    product = Product.query.get(id)
    
    if product.account_id == current_user.id:
        Order.query.filter_by(product_id=product.id).delete()  
        db.session.delete(product)
        try:
            db.session().commit()
        except:
            db.session.rollback()
  
    return redirect(url_for("auth_user"))

# change description
@app.route("/products/change/", methods=["POST"])
@login_required
def products_set_description():
    id = request.form.get("change_id")
    new = request.form.get("newdesc")

    # validate new description lenght
    if len(new) > 45:
        flash("New description must be below 45 characters.", "long")
        item_count = User.count_items(current_user.id)
        order_products = db.session.query(Order, Product).join(Product).join(User).filter(Order.account_id == current_user.id).all()
        return render_template("auth/user.html", item_count=item_count, orders = order_products, user = current_user)

    product = Product.query.get(id)    

    if new and product.account_id == current_user.id:
        product.description = new

        try:
            db.session().commit()
        except:
            db.session.rollback()
  
    return redirect(url_for("auth_user"))

# post product
@app.route("/products/", methods=["POST"])
@login_required
def products_create():
    form = ProductForm(request.form)

    if not form.validate():
        return render_template("products/new.html", form = form, categories = Category.query.all())

    # selection from form & dropdown list
    category_name = request.form.get("select")

    # get category
    category = Category.query.filter_by(name=category_name).first()

    product = Product(form.name.data, form.price.data, 
    form.description.data)
    product.account_id = current_user.id
    product.category_id = category.id

    db.session().add(product)

    try:
        db.session().commit()
    except:
        db.session.rollback()
  
    return redirect(url_for("auth_user"))
