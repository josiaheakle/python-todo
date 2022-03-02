from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Email, Length

class RegisterForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired(), Length(6, 24, "Must be between 6 and 24 characters")])
    email = StringField("Email", validators=[InputRequired(), Email()])
    password = PasswordField("Password", validators=[InputRequired(), Length(6, 24, "Must be between 6 and 24 characters"), ])
    firstName = StringField("First Name", validators=[InputRequired()])
    lastName = StringField("Last Name", validators=[InputRequired()])
    submit = SubmitField("Submit")
