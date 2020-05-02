from flask_wtf import FlaskForm
from wtforms import Form, BooleanField, SubmitField
from wtforms_components import TimeField, SelectField
from wtforms.validators import DataRequired

def minuteToAmPm(minute):
    total = minute / 60
    hr = minute // 60
    min = minute % 60
    start_time = 9
    if (min == 0) :
        min = '00'
    if (start_time+total < 13) :
        return f'{int(start_time+total)}:{min} A.M.'
    return f'{int(start_time+total-12)}:{min} P.M.'

def initTimeRange():
    rangeChoices = []
    time = 0 #pretending 9am is at 0 value
    minute = 15 #each section of time is 15 minute
    while minute*time <= 13*60: #range is from 9am to 10pm ~ 13hrs to 13*60min
        pair = (minute*time, minuteToAmPm(minute*time))
        rangeChoices.extend([pair])
        time = time + 1
    return rangeChoices
 
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
    "List of tupple of time such as [(0,'9:0AM'), (15,'9:15AM'), (30,'9:30AM'),... (240,'1:0PM'),...]"
    start_time = SelectField('Choose a time',choices=timeRange)
    """Start of working hour"""
    end_time = SelectField('Choose a time',choices=timeRange)
    """End of working hour"""

    # fifteen = BooleanField('15 minutes')
    # """15 minutes allowed Boolean field"""
    # thirty = BooleanField('30 minutes')
    # """30 minutes allowed Boolean field"""
    # sixty = BooleanField('60 minutes')
    # """60 minutes allowed Boolean field"""

    emailconfirm = BooleanField('Email Confirmation?')
    """Email confirmation check box"""
    submit = SubmitField('Save Changes')
    """Submit to Save changes"""

