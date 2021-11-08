from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, validators, SubmitField, DateTimeField


class UserForm(FlaskForm):
    name = StringField('Name', [validators.Length(min=4, max=255), validators.DataRequired()])
    email = StringField('Email Address', [validators.Length(min=6, max=255), validators.DataRequired()])
    phone = StringField('Phone Number', [validators.Length(min=8, max=14)])
    active = BooleanField('Is Active ?')
    confirmed_at = DateTimeField('Confirmed at', format="%Y-%m-%d %H:%M:%S", default=datetime.today)
    submit = SubmitField('Submit')

