from flask_wtf from FlaskForm
from wtforms from StringField


class RegistrationForm(FlaskForm):

    username = StringField('Username')
