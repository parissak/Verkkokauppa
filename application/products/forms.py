from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, IntegerField
from wtforms import validators, fields
from decimal import Decimal, DecimalException
 
class CustomDecimalField(fields.DecimalField):
    def process_formdata(self, data):   
        try:
            data[0] = round(Decimal(data[0].replace(",", ".")), 2)
            return super(CustomDecimalField, self).process_formdata(data) 
        except (DecimalException, ValueError):     
            data = None
            raise ValueError(self.gettext('Not a valid decimal number')) 
 
class ProductForm(FlaskForm):
    name = StringField("Product name", [validators.Length(min=2, max=20)])
    price = CustomDecimalField("Price", validators=[validators.NumberRange(min=0.009, max=100000, 
    message="Price must be between 0.01 and 100000")])
    description = StringField("Description", [validators.Length(max=45)])
 
    class Meta:
        csrf = False

class SearchForm(FlaskForm):
    search = StringField("Name")