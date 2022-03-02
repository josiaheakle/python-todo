
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateField, SubmitField
from wtforms.validators import InputRequired, Length

class TodoForm(FlaskForm):
    title = StringField("Title", validators=[InputRequired(), Length(0, 256, "Must be less than 256 characters in length.")])
    description = TextAreaField("Description", validators=[InputRequired(), Length(0, 1024, "Must be less than 1024 characters in length.")])
    dueDate = DateField("Due Date")
    submit = SubmitField("Submit")