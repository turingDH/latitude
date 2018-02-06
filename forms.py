from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class SignupForm(Form):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email("Please enter valid email address")])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, message="Must be at least 8 characters")])
    submit = SubmitField('Sign up!')