from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    # checks
    # 1. make sure something is inputted
    # 2. make sure it is valid
    username = StringField('Username',
                            validators=[DataRequired(), Length(min=1, max=20)])

    email = StringField('Email',validators=[DataRequired(), Email()])

    password = PasswordField('Password',validators=[DataRequired()])

    confirm_password = PasswordField('Confirm Password',
                                    validators=[DataRequired(),
                                                EqualTo('password')])

    submit = SubmitField('Sign Up')

class LogInForm(FlaskForm):
    # checks
    # 1. make sure something is inputted
    # 2. make sure it is valid

    email = StringField('Email',validators=[DataRequired(), Email()])

    password = PasswordField('Password',validators=[DataRequired()])

    remember = BooleanField('Remember Me')

    submit = SubmitField('Login In')
