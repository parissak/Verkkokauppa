from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user
from flask_login import current_user, login_required

from sqlalchemy.sql import text

from application import app, db
from application.auth.models import User
from application.auth.forms import LoginForm, RegistrationForm

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()

    if not user:
        return render_template("auth/loginform.html", form = form,
                               error = "No such username or password")

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
        return render_template("auth/regform.html", form = form)
        

    user = User(form.name.data, form.username.data, form.password.data)
  
    db.session().add(user)
    db.session().commit()

    return redirect(url_for("index"))

# return user page
@app.route("/auth/user")
@login_required
def auth_user():
    u = current_user  
    item_count = User.count_items(current_user.id)

    return render_template("auth/user.html", item_count=item_count, user = u)
