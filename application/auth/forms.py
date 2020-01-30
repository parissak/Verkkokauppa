from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField
from wtforms import validators
  
class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")
  
    class Meta:
        csrf = False


class RegistrationForm(FlaskForm):
    name = StringField("Name", [validators.Length(min=2, max=20)])
    username = StringField("Username", [validators.Length(min=2, max=20)])
    password = PasswordField("Password", [validators.Length(min=2, max=20)])
  
    class Meta:
        csrf = False
