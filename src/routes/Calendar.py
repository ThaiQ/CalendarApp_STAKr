from flask import render_template, request, jsonify
from src import app
import calendar
from datetime import datetime

@app.route("/calendar")
def Calendar():
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
    
    return render_template('Calendar/calendar.html', 
    dates = dates, days = days, month=[currentMonth, months[currentMonth]], year = currentYear)

@app.route("/getEventsOnMonth", methods=['GET'])
def getEventsOnMonth():
    monthBuckets = []
    
    date = 0
    while date < 33:
        monthBuckets.append([])
        date = date + 1

    monthBuckets[4] = [
        {
            "name:" : "n1",
            "date " : "1/2"
        },
        {
            "name:" : "n2",
            "date " : "1/2"
        }
    ]

    return jsonify([monthBuckets])
