from . import datetime
from . import FlaskForm
from . import BooleanField, StringField, TextAreaField, \
                    IntegerField, SelectMultipleField, PasswordField, \
                    validators, SubmitField, DateTimeField

class UserForm(FlaskForm):
    id = IntegerField(default=0)
    name = StringField('Name', [validators.Length(min=4, max=255), validators.DataRequired()])
    email = StringField('Email Address', [validators.Length(min=6, max=255), validators.DataRequired()])
    phone = StringField('Phone Number', [validators.Length(min=8, max=14)])
    role = SelectMultipleField('Role', coerce=int, default = [1])
    active = BooleanField('Is Active ?')
    confirmed_at = DateTimeField('Confirmed at', format="%Y-%m-%d %H:%M:%S", default=datetime.today)
    submit = SubmitField('Submit')

class RoleForm(FlaskForm):
    id = IntegerField(default=0)
    name = StringField('Name', [validators.Length(min=4, max=80), validators.DataRequired()])
    description = TextAreaField('Description', default='', render_kw={'rows':5})
    submit = SubmitField('Submit')