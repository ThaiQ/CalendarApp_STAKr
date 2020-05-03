from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from src.utils import initTimeRange, minuteToAmPm
from wtforms_components import TimeField, SelectField
 
class EventForm(FlaskForm):
    guest_name = StringField('Your name', validators=[DataRequired()])
    """Guest Name"""
    event_name = StringField('Title of Appointment (optional)', validators=[DataRequired()])
    """Name of event (optional)"""
    event_description = StringField('Description')
    """Event's description"""

    timeRange = initTimeRange()
    "List of tuple of time such as [(0,'9:0AM'), (15,'9:15AM'), (30,'9:30AM'),... (240,'1:0PM'),...]"
    start_time = SelectField('Start time', choices=timeRange)
    """Start of working hour"""
    end_time = SelectField('End time', choices=timeRange)
    """End of working hour"""

    submit = SubmitField('Make Appointment')
    """Sign-in button"""
