from flask import render_template
from src import app
import calendar

@app.route("/calendar")
def Calendar():
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    months = ["", "January", "Feburary", "March", "April", "May", "Jun",
     "July", "August", "September", "October", "Novermber", "December"]
    fullMonth = calendar.monthcalendar(2020,4)
    dates = []
    for week in fullMonth:
        dates.extend(week)
    
    return render_template('Calendar/calendar.html', 
    dates = dates, days = days, month=months[4], year = 2020)
