from flask import render_template, request, jsonify, redirect, request, flash
from flask_login import current_user
from src.schemas import User, Event
from src.forms import EventForm
from src.utils import minuteToAmPm
from src import app, db
from datetime import datetime
import calendar

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
"""Array of days"""
months = ["", "January", "Feburary", "March", "April", "May", "Jun",
    "July", "August", "September", "October", "Novermber", "December"]
"""Array of months"""

@app.route("/calendar")
def CalendarAdmin():
    """
    Home of user and also the meeting page.

    Parameters:
        N/A

    Returns:
        Rendered calendar and meetings of the month
    """
    currentMonth = request.args.get('month')
    currentYear = request.args.get('year')
    if (currentYear is None): currentYear = int(datetime.now().year)
    else: currentYear = int(currentYear)

    if currentMonth is None: currentMonth = int(datetime.now().month)
    else : currentMonth = int(currentMonth)
    #translate months
    if (currentMonth > 12): 
        currentMonth = 1
        currentYear = currentYear + 1
    elif (currentMonth < 1): 
        currentMonth = 12
        currentYear = currentYear - 1
    #getting weeks of the month
    fullMonth = calendar.monthcalendar(currentYear, currentMonth)
    dates = []
    for week in fullMonth:
        dates.extend(week)
    #directions
    if current_user.is_authenticated:
        return render_template('Calendar/admin-calendar.html', username=current_user.username,
        dates = dates, days = days, month=[currentMonth, months[currentMonth]], year = currentYear)
    return redirect('/')

@app.route("/<username>", methods=['GET', 'POST'])
def CalendarUser(username):
    """
    Allow to book appointments from a user.

    Parameters:
        username: user's username (AKA. host's username)

    Returns:
        Rendered calendar and appointment slots of the month
    """
    currentMonth = request.args.get('month')
    currentYear = request.args.get('year')
    if (currentYear is None): currentYear = int(datetime.now().year)
    else: currentYear = int(currentYear)

    if currentMonth is None: currentMonth = int(datetime.now().month)
    else : currentMonth = int(currentMonth)

    if (currentMonth > 12): 
        currentMonth = 1
        currentYear = currentYear + 1
    elif (currentMonth < 1): 
        currentMonth = 12
        currentYear = currentYear - 1
    #translate month
    fullMonth = calendar.monthcalendar(currentYear, currentMonth)

    dates = []
    for week in fullMonth:
        dates.extend(week)
    #get user and their apointment-slots
    user = User.query.filter_by(username=username).first()
    form = EventForm()
    if request.method == "POST" and form.guest_name.data is not None and form.event_date.data is not None and int(request.form['open-slots'].split()[0])>-1:
        name = form.event_name.data
        description = form.event_description.data
        if name is None or name == '': name = form.guest_name.data
        if description is None or description == '': description = "N/A"
        times = request.form['open-slots'].split()
        #create events
        event = Event(
            guest=form.guest_name.data,
            event_name=name,
            event_description=description,
            event_date=form.event_date.data,
            event_month=form.event_month.data,
            event_year=form.event_year.data,
            start_hour = int(times[0]),
            end_hour = int(times[1]),
            length = int(times[1])-int(times[0]),
            host = user.username
        )
        db.session.add(event)
        db.session.commit()
        return redirect('/')
    #direction
    if user is not None:
        return render_template('Calendar/user-calendar.html', user = user, form = form,
        dates = dates, days = days, month=[currentMonth, months[currentMonth]], year = currentYear)
    return redirect('/')

@app.route("/getEventsOnMonth/<username>/<month>/<year>", methods=['GET'])
def getEventsOnMonth(username, month, year):
    """
    Get all events of a month from a user.

    Parameters:
        username: user's username (AKA. host's username)
        month: month to get
        year: year to get

    Returns:
        jason of a direct bucket of the month
        where each bucket is a list of events of that date
    """
    monthBuckets = []
    date = 0
    while date < 33:
        monthBuckets.append([])
        date = date + 1
    events = Event.query.filter_by(host=username, event_month=month, event_year=year).all()
    for event in events:
        monthBuckets[event.event_date].extend([{
            "guest":event.guest,
            "host":event.host,
            "event_name": event.event_name,
            "event_date": event.event_date,
            "event_description" : event.event_description,
            "length": event.length,
            "event_month": event.event_month,
            "event_year": event.event_year,
            "start_hour": event.start_hour,
            "end_hour": event.end_hour,
        }])
    return jsonify([monthBuckets])

@app.route("/getslots/<username>/<month>/<date>/<year>", methods=['GET'])
def getOpenSlots(username, month, date, year):
    """
    Get open slots for appointment from a user
    from a date/month/year

    Parameters:
        username: user's username (AKA. host's username)
        month: month to get
        date: date to get
        year: year to get

    Returns:
        jason of a list of paired tuples where:
        [((start_time, end_time), '9AM to 10PM'),...]
    """
    user = User.query.filter_by(username=username).first()
    monthBuckets = Event.query.filter_by(host=username, event_date=date, event_month=month, event_year=year).all()
    if user:
        slotsBuckets = []
        startTime = user.start_available
        endTime = startTime
        while endTime + user.meeting_length <= user.end_available:
            endTime = startTime + user.meeting_length
            label = f'{minuteToAmPm(startTime)} to {minuteToAmPm(endTime)}'
            slotsBuckets.append([((startTime,endTime),label)])
            startTime = endTime
        # #filter beginning and end times
        newList = []
        for pair in slotsBuckets:
            start_time = pair[0][0][0]
            end_time = pair[0][0][1]
            if (user.start_available<=start_time and end_time<=user.end_available): newList.append(pair)
        slotsBuckets = newList
        #filter used times of other events
        for event in monthBuckets:
            newList = []
            for pair in slotsBuckets:
                start_time = pair[0][0][0]
                end_time = pair[0][0][1]
                if (start_time<=event.start_hour and event.end_hour<=end_time) : pass
                elif (start_time<event.start_hour and event.start_hour<end_time and end_time<event.end_hour) : pass
                elif (event.start_hour<start_time and startTime<event.end_hour and event.end_hour<end_time) : pass
                else : newList.append(pair)
            slotsBuckets = newList
        return jsonify(slotsBuckets)
    return jsonify([])