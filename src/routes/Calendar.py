from flask import render_template, request, jsonify, redirect
from flask_login import current_user
from src.schemas import User
from src.forms import EventForm
from src import app
import calendar
from datetime import datetime

@app.route("/calendar")
def CalendarAdmin():
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
    
    fullMonth = calendar.monthcalendar(currentYear, currentMonth)

    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    months = ["", "January", "Feburary", "March", "April", "May", "Jun",
     "July", "August", "September", "October", "Novermber", "December"]
    dates = []
    for week in fullMonth:
        dates.extend(week)
    
    if current_user.is_authenticated:
        return render_template('Calendar/admin-calendar.html', 
        dates = dates, days = days, month=[currentMonth, months[currentMonth]], year = currentYear)
    return redirect('/')


@app.route("/calendar/<username>")
def CalendarUser(username):
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
    
    fullMonth = calendar.monthcalendar(currentYear, currentMonth)

    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    months = ["", "January", "Feburary", "March", "April", "May", "Jun",
     "July", "August", "September", "October", "Novermber", "December"]
    dates = []
    for week in fullMonth:
        dates.extend(week)
    
    user = User.query.filter_by(username=username).first()
    user = {
        "start": 0,
        "end": 1800,
        "duration": 60
    }
    form = EventForm()
    if user is not None:
        return render_template('Calendar/user-calendar.html', user = user, form = form,
        dates = dates, days = days, month=[currentMonth, months[currentMonth]], year = currentYear)
    return redirect('/')

@app.route("/getEventsOnMonth", methods=['GET'])
def getEventsOnMonth():
    monthBuckets = []
    
    date = 0
    while date < 33:
        monthBuckets.append([])
        date = date + 1

    monthBuckets[4] = [
        {
            "name" : "PResident and dev team",
            "date" : 1,
            "month" : 4,
            "year"  : 2000,
            "start_time": "9A.M",
            "end_time": "9:10A.M"
        },
        {
            "name" : "PResident and dev teamPResident and dev team",
            "date" : 1,
            "month" : 4,
            "year"  : 2000,
            "start_time": "9A.M",
            "end_time": "9:10A.M"
        }
    ]

    return jsonify([monthBuckets])
