from src import db
from datetime import datetime

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    """event's id"""
    guest = db.Column(db.String(250), nullable=False)
    """guest's name"""
    host = db.Column(db.String(250), nullable=False)
    """host's name"""
    host_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    """host's id"""
    event_name = db.Column(db.String(250), nullable=False)
    """event's name"""
    event_description = db.Column(db.String(2000), default="")
    """event's description"""
    event_date = db.Column(db.Integer, nullable=False)
    """event's date"""
    event_month = db.Column(db.Integer, nullable=False)
    """event's month"""
    event_year = db.Column(db.Integer, nullable=False)
    """event's year"""
    start_hour = db.Column(db.Integer, nullable=False)
    """event's start hour"""
    end_hour = db.Column(db.Integer, nullable=False)
    """event's end hour"""
    length = db.Column(db.Integer)
    """event's  durations"""

    def __repf__(self):
        return '<Event: {} {} {}>'.format(self.guest, self.event_name, self.event_description, self.event_month, self.event_name, self.event_year, self.length)
