from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms import validators

class ProductForm(FlaskForm):
    name = StringField("Product name", [validators.Length(min=2, max=20)])
    price = IntegerField("Price", [validators.DataRequired(message="Field cannot be empty or non numerical")])
    description = StringField("Description", [validators.Length(max=30)])
 
    class Meta:
        csrf = False

# tobeimplemented
#class SearchForm(FlaskForm):
#    search = StringField("Name")