from . import datetime
from . import FlaskForm
from . import BooleanField, StringField, TextAreaField, \
                    IntegerField, SelectMultipleField, PasswordField, \
                    validators, SubmitField, DateTimeField, FloatField

class SensorForm(FlaskForm):
    id = IntegerField(default=0)
    name = StringField('Name', [validators.Length(min=4, max=80), validators.DataRequired()])
    device_no = StringField('Device No', [validators.Length(min=4, max=80), validators.DataRequired()])
    device_type = StringField('Device Type', [validators.Length(min=4, max=80)])
    time = DateTimeField('Send On')
    value = FloatField('Value')
    submit = SubmitField('Submit')