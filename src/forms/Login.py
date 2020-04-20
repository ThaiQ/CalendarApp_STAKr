from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
 
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    """Username for login"""
    password = PasswordField('Password', validators=[DataRequired()])
    """Password to login"""
    remember_me = BooleanField('Remember Me')
    """Remember me check box"""
    submit = SubmitField('Sign In')
    """Sign-in button"""
