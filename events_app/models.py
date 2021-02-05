"""Create database models to represent tables."""
from events_app import db
from sqlalchemy.orm import backref
import enum

class Guest(db.Model):
    """Guest Model"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False, unique=True)
    phone = db.Column(db.Integer, nullable=False, unique=True)

    events_attending = db.relationship('Event', secondary='guest_event_table', back_populates='guests')

    def __str__(self):
        return f'<Guest: {self.name}>'

    def __repr__(self):
        return f'<Guest: {self.name}>'


# STRETCH CHALLENGE: Add a field `event_type` as an Enum column that denotes the
# type of event (Party, Study, Networking, etc)

class Event(db.Model):
    """Event Model"""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(80), nullable=False)
    date_and_time = db.Column(db.DateTime, nullable=False)

    guests = db.relationship('Guest', secondary='guest_event_table', back_populates='events_attending')

    def __str__(self):
        return f'<Event: {self.title}, Desc: {self.description}>'

    def __repr__(self):
        return f'<Event: {self.title}, Desc: {self.description}>'


guest_event_table = db.Table('guest_event_table',
    db.Column('event_id', db.Integer, db.ForeignKey('event.id')),
    db.Column('guest_id', db.Integer, db.ForeignKey('guest.id'))
)