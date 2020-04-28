from src import db
from src import login
from datetime import datetime

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    """event's id"""
    guest = db.Column(db.String(70), index=True, unique=True)
    event_name = db.Column(db.String(100), nullable=False)
    """event's name"""
    event_description = db.Column(db.Text(2000), nullable=False)
    """event's description"""
    event_date = db.Column(db.Date, nullable=False, default=date.utcnow)
    event_month = db.Column(db.Month, nullable=False, default=month.utcnow)
    event_year = db.Column(db.Year, nullable=False, default=year.utcnow)
    start_hour = db.Column(db.Hour, nullable=False, default=time.utcnow)
    end_hour = db.Column(db.Hour, nullable=False, default=time.utcnow)
    """Event's datetime"""
    length = db.Column(db.Integer)

    def __repf__(self):
        return '<Event: {} {} {}>'.format(self.guest, self.event_name, self.event_description, self.event_month, self.event_name, self.event_year, self.length)
