from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user, login_required
from application import app, db
from application.auth.models import User
from application.auth.forms import LoginForm, RegistrationForm
from application.orders.models import Order
from application.products.models import Product


@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()

    if not user:
        flash("No such username or password", "not_found")
        return render_template("auth/loginform.html", form = form)

    login_user(user)

    return redirect(url_for("index"))

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index")) 

# return RegistrationForm
@app.route("/auth/registration")
def auth_registration_form():
    return render_template("auth/regform.html", form = RegistrationForm())

# post registration
@app.route("/auth/registration/", methods=["POST"])
def auth_registration_create():
    form = RegistrationForm(request.form)
        
    if not form.validate():
        flash("Please correct the errors in order to continue.")
        return render_template("auth/regform.html", form = form)

    # checks if username exists
    username_exists = User.query.filter_by(username=form.username.data).first()
    if username_exists:
        flash("Username exists, please choose another one.")
        return render_template("auth/regform.html", form = form)
        
    new_user = User(form.name.data, form.username.data, form.password.data)
  
    db.session().add(new_user)
    try:
        db.session().commit()       
    except:
        db.session.rollback() 
    
    return redirect(url_for("index"))

# return user page
@app.route("/auth/user")
@login_required
def auth_user():
    user = current_user  
    item_count = User.count_items(current_user.id)
    order_products = db.session.query(Order, Product).join(Product).join(User).filter(Order.account_id == user.id).all()

    return render_template("auth/user.html", item_count=item_count, orders = order_products, user = user)
