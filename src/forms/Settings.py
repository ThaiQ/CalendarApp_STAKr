from flask_wtf import FlaskForm
from wtforms import Form, BooleanField, SubmitField
from wtforms_components import TimeField, SelectField
from wtforms.validators import DataRequired
from src.utils import minuteToAmPm, initTimeRange
 
class SettingsForm(FlaskForm):
    # start_time = TimeField('Start Time Availability', validators=[DataRequired()])
    # """Time field for Availability"""
    # end_time = TimeField('End Time Availability', validators=[DataRequired()])
    # """Time field for Availability"""

    choices = [(15, '15 minute'), (30,'30 minute'), (60, '60 minute')]
    """Meeting duration list [(dataValue, textLabel), (value, textLabel)]"""
    duration = SelectField('Choose a time',choices=choices)
    """Meeting duration"""

    timeRange = initTimeRange()
    "List of tuple of time such as [(0,'9:0AM'), (15,'9:15AM'), (30,'9:30AM'),... (240,'1:0PM'),...]"
    start_time = SelectField('Choose a time', choices=timeRange)
    """Start of working hour"""
    end_time = SelectField('Choose a time', choices=timeRange)
    """End of working hour"""

    # fifteen = BooleanField('15 minutes')
    # """15 minutes allowed Boolean field"""
    # thirty = BooleanField('30 minutes')
    # """30 minutes allowed Boolean field"""
    # sixty = BooleanField('60 minutes')
    # """60 minutes allowed Boolean field"""

    emailconfirm = BooleanField('Email Confirmation?')
    """Email confirmation check box"""
    delete = SubmitField('Delete Account?')
    submit = SubmitField('Save Changes')
    """Submit to Save changes"""


