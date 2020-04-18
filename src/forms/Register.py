from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo

class RegistrationForm(FlaskForm):
    firstname= StringField('Firstname', validators=[DataRequired()])
    """User firstname"""
    lastname= StringField('Lastname', validators=[DataRequired()])
    """User lastname"""
    username = StringField('Username', validators=[DataRequired()])
    """Username for login"""
    email = StringField('Email', validators=[DataRequired(), Email()])
    """Email for scheduling,confirmation, and validation"""
    email2 = StringField('Repeat Email', validators=[DataRequired(), EqualTo('email')])
    """Repeat of the first email, must equal 'email'"""
    password = PasswordField('Password', validators=[DataRequired()])
    """Desired password, raw and not hashed"""
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    """Repeat of 'password'"""
    submit = SubmitField('Register')
    """Submit button"""