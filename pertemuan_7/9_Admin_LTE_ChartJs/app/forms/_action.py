from . import FlaskForm
from . import SubmitField

class ActionTable(FlaskForm):
    activate = SubmitField('Activate')
    deactivate = SubmitField('Deactivate')
    delete = SubmitField('Delete')