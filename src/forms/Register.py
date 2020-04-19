from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from src.schemas import User

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
    
    '''
        Validate Username
            Makes sure the username is not in the database
        
        Parameters
            self, username
        
        Returns
            ValidationError if the username already exists
    '''
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')
    
    
    '''
        Validate Email
            Makes sure the email does not exist in the database
        
        Parameters
            self, email
        
        Returns
            ValidationError if the email already exists in the database
    '''
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')