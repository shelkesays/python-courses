from flask_wtf import Form
from wtforms import PasswordField
from wtforms import SubmitField
from wtforms.fields.html5 import EmailField
from wtforms import validators
from wtforms import TextField


class RegistrationForm(Form):
    email = EmailField('email', validators=[validators.DataRequired(), validators.Email()])
    password = PasswordField('password', validators=[validators.DataRequired(),
    	validators.Length(min=8, message="Please choose a password of at least 8 characters")])
    password2 = PasswordField('password2', validators=[validators.DataRequired(),
    	validators.EqualTo('password', message='Passwords must match')])
    submit = SubmitField('submit', [validators.DataRequired()])


class LoginForm(Form):
    email = EmailField('loginemail', validators=[validators.DataRequired(), validators.Email()])
    password = PasswordField('loginpassword', validators=[validators.DataRequired(message="Password field is required")])
    submit = SubmitField('loginsubmit', [validators.DataRequired()])


class CreateTableForm(Form):
	tablenumber = TextField('tablenumber', validators=[validators.DataRequired()])
	submit = SubmitField('createtablesubmit', validators=[validators.DataRequired()])