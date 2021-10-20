from wtforms import Form, BooleanField, StringField, PasswordField, validators, SubmitField


class UserForm(Form):
    name = StringField('Name', [validators.Length(min=4, max=50), validators.DataRequired()])
    email = StringField('Email Address', [validators.Length(min=6, max=50), validators.DataRequired()])
    phone = StringField('Phone Number', [validators.Length(min=8, max=14)])
    password = PasswordField('New Password', [validators.InputRequired(), 
                    validators.EqualTo('confirm', message='Passwords must match')])
    confirm  = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])

    submit = SubmitField('Submit')

