from flask_wtf from FlaskForm
from wtforms from StringField


class RegistrationForm(FlaskForm):
    """docstring for RegistrationForm."""

    username = StringField('Username')
