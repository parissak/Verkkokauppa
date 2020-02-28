from flask import redirect, render_template, request, url_for, flash
from flask_login import current_user, login_required
from application import app, db
from application.products.models import Product
from application.categories.models import Category
from application.orders.models import Order
from application.auth.models import User
from application.products.forms import ProductForm
from application.products.forms import SearchForm
from sqlalchemy.sql import text


# list & search
@app.route("/products", methods=["GET", "POST"])
def products_index():

    # get three most ordered
    stmt = text(
        'Select product.name FROM "order" '
        "JOIN Product on Product.id = product_id "
        "JOIN Account ON account.id = product.account_id "
        "GROUP BY product.id "
        "ORDER BY COUNT(product.id) "
        "DESC LIMIT 3;"
    )
    res = db.engine.execute(stmt)
    items = res
    top_three = ""
    count = 0
    for x in items:
        count += 1
        top_three += str(count) + ". " + str(x[0]) + " "

    # pagination
    page = request.args.get("page", 1, type=int)

    if request.method == "POST":
        form = SearchForm(request.form)
        product_name = request.form.get("search")

        if not product_name:
            result = Product.query.order_by(Product.date_created.desc()).paginate(
                page, 20, False)
        else:
            result = (Product.query.order_by(Product.date_created.desc())
                .filter_by(name=product_name)
                .paginate(page, 20, False))

    if request.method == "GET":
        result = Product.query.order_by(Product.date_created.desc()).paginate(
            page, 20, False)

    return render_template("products/list.html", form=SearchForm(), products=result, top_three=top_three)


# new
@app.route("/products/new/")
@login_required
def products_form():
    return render_template(
        "products/new.html", form=ProductForm(), categories=Category.query.all()
    )


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
        order_products = (
            db.session.query(Order, Product)
            .join(Product)
            .join(User)
            .filter(Order.account_id == current_user.id)
            .all()
        )
        order_count = len(order_products)
        return render_template(
            "auth/user.html",
            item_count=item_count,
            order_count=order_count,
            orders=order_products,
            user=current_user,
        )

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
        return render_template(
            "products/new.html", form=form, categories=Category.query.all()
        )

    # selection from form & dropdown list
    category_name = request.form.get("select")

    # get category
    category = Category.query.filter_by(name=category_name).first()

    product = Product(form.name.data, form.price.data, form.description.data)
    product.account_id = current_user.id
    product.category_id = category.id

    db.session().add(product)

    try:
        db.session().commit()
    except:
        db.session.rollback()

    return redirect(url_for("auth_user"))
