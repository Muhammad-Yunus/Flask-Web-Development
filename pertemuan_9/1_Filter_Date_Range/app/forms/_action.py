from . import FlaskForm
from . import SubmitField, DateTimeField, StringField, BooleanField

class ActionTable(FlaskForm):
    activate = SubmitField('Activate')
    deactivate = SubmitField('Deactivate')
    delete = SubmitField('Delete')


class FilterDateForm(FlaskForm):
    from_date =  DateTimeField('From') 
    to_date =  DateTimeField('To')
    quick_range = BooleanField('Quick Range')
    data = StringField('Data')
    submit = SubmitField('Apply')