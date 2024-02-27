from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired, URL


class AddTodoForm(FlaskForm):
    todo = StringField('', validators=[DataRequired()],render_kw={'class': "form-control"})
    submit = SubmitField('Add ➕', render_kw={'class': "btn-info"})
