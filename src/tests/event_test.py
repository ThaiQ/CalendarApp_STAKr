from src.schemas import Event
from src import db

valid_event = {
    'host' : 'host',
    'guest' : 'guest',
    'event_date' : 1,
    'event_month' : 2,
    'event_year' : 3,
    'start_hour' : 1,
    'end_hour': 2,
    'event_name': 'event_name'
}

new_event = {
    'host' : 'new host ok ?',
    'guest' : 'new guest ok ?',
}

def test_createEvent():
    event = Event(
    guest = valid_event['guest'],
    event_date = valid_event['event_date'],
    event_month = valid_event['event_month'],
    event_year = valid_event['event_year'],
    start_hour = valid_event['start_hour'],
    end_hour = valid_event['end_hour'],
    host = valid_event['host'],
    event_name = valid_event['event_name'],
    event_description='',
    )
    #commit data
    db.session.add(event)
    db.session.commit()
    findEvent = Event.query.filter_by(host=valid_event['host'], guest = valid_event['guest'], event_date = valid_event['event_date']).first()
    #assert saved data
    assert findEvent.guest == valid_event['guest']
    assert findEvent.event_date == valid_event['event_date']
    assert findEvent.event_month == valid_event['event_month']
    assert findEvent.event_year == valid_event['event_year']
    assert findEvent.start_hour == valid_event['start_hour']
    assert findEvent.end_hour == valid_event['end_hour']
    assert findEvent.host == valid_event['host']
    assert findEvent.event_name == valid_event['event_name']
    assert findEvent.event_description == ''

def test_updateEvent():
    findEvent = Event.query.filter_by(host=valid_event['host'], guest = valid_event['guest'], event_date = valid_event['event_date']).first()
    findEvent.guest = new_event['guest']
    findEvent.host = new_event['host']
    db.session.commit()
    findEvent = Event.query.filter_by(host=new_event['host'], guest = new_event['guest'], event_date = valid_event['event_date']).first()
    assert findEvent.guest == new_event['guest']
    assert findEvent.host == new_event['host']

def test_deleteEvent():
    #delete event
    findEvent = Event.query.filter_by(host=new_event['host'], guest = new_event['guest'], event_date = valid_event['event_date']).first()
    assert findEvent is not None
    db.session.delete(findEvent)
    db.session.commit()
    #confirm event is deleted
    findEvent = Event.query.filter_by(host=new_event['host'], guest = new_event['guest'], event_date = valid_event['event_date']).first()
    assert findEvent is None