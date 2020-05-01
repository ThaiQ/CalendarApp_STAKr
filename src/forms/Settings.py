from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired
 
class SettingsForm(FlaskForm):
    available = StringField('Availability between 9am-10pm (ex. 9am-4pm)', validators=[DataRequired()])
    """String field for Availability"""
    fifteen = BooleanField('15 minutes')
    """15 minutes allowed Boolean field"""
    thirty = BooleanField('30 minutes')
    """30 minutes allowed Boolean field"""
    sixty = BooleanField('60 minutes')
    """60 minutes allowed Boolean field"""
    emailconfirm = BooleanField('Email Confirmation?')
    """Email confirmation check box"""
    submit = SubmitField('Save Changes')
    """Submit to Save changes"""
