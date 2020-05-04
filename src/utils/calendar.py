from src.schemas import User
from flask_login import current_user

def minuteToAmPm(minute):
    """
    translating from minute to AM or PM
    between 9AM and 10PM

    Parameters:
        minute (int): total number of minute starting from 9AM (0 minute)
    
    return:
        between 9AM and 10PM
    """
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
    """
    tuple of working times from 9AM to 10PM

    Parameters:
        N/A
    
    return:
        list of tuple of paired times between 9AM to 10PM
        [(0,9:00AM),(15,9:15AM),(30,9:30AM),...]
    """
    rangeChoices = []
    time = 0 #pretending 9am is at 0 value
    minute = 15 #each section of time is 15 minute
    while minute*time <= 13*60: #range is from 9am to 10pm ~ 13hrs to 13*60min
        pair = (minute*time, minuteToAmPm(minute*time))
        rangeChoices.extend([pair])
        time = time + 1
    return rangeChoices