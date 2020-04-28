from datetime import datetime

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    """event's id"""
    guest = db.Column(db.String(70), nullable=False)
    """guest's name"""
    event_name = db.Column(db.String(100), nullable=False)
    """event's name"""
    event_description = db.Column(db.Text(2000), nullable=False)
    """event's description"""
    event_date = db.Column(db.Date, nullable=False, date.utcnow)
    """event's date"""
    event_month = db.Column(db.Month, nullable=False, month.utcnow)
    """event's month"""
    event_year = db.Column(db.Year, nullable=False, year.utcnow)
    """event's year"""
    start_hour = db.Column(db.Hour, nullable=False, time.utcnow)
    """event's start hour"""
    end_hour = db.Column(db.Hour, nullable=False, time.utcnow)
    """event's end hour"""
    length = db.Column(db.Integer)
    """event's  durations"""

    def __repf__(self):
        return '<Event: {} {} {}>'.format(self.guest, self.event_name, self.event_description, self.event_month, self.event_name, self.event_year, self.length)
