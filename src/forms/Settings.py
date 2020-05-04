from flask_wtf import FlaskForm
from wtforms import BooleanField, SubmitField
from wtforms_components import SelectField
from src.utils import initTimeRange
 
class SettingsForm(FlaskForm):
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

    emailconfirm = BooleanField('Email Confirmation?')
    """Email confirmation check box"""
    delete = SubmitField('Delete Account?')
    """Delete Account"""
    submit = SubmitField('Save Changes')
    """Submit to Save changes"""


