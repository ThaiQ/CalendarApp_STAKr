from src.schemas import User
from flask_login import current_user

def minuteToAmPm(minute):
    total = minute / 60
    hr = minute // 60
    min = minute % 60
    start_time = 9
    if (min == 0) :
        min = '00'
    if (start_time+total < 13) :
        if start_time + hr == 12:
            return f'{int(start_time+total)}:{min} P.M.'
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