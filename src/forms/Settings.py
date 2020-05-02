from flask_wtf import FlaskForm
from wtforms import Form, BooleanField, SubmitField
from wtforms_components import TimeField
from wtforms.validators import DataRequired
 
class SettingsForm(FlaskForm):
    start_time = TimeField('Start Time Availability', validators=[DataRequired()])
	end_time = TimeField('End Time Availability' validators=[DataRequired()])
	"""Time field for Availability"""
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
