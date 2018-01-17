"""
    filename: 
    date:     
    :copyright: (c) 2017 by binjie chen.
"""

from flask import current_app
from app import db


class Developer(db.Model):
    __tablename__ = 'developers'
    id = db.Column(db.Integer, primary_key=True)
    dev_key = db.Column(db.String(40), unique=True, index=True)
    platform = db.Column(db.String(50))
    platform_id = db.Column(db.String(40), unique=True)
    username = db.Column(db.String(150), index=True)
    integrations = db.relationship('Integration', backref='developer')
    channels = db.relationship('Channel', backref='developer')


class Integration(db.Model):
    __tablename__ = 'integrations'
    id = db.Column(db.Integer, primary_key=True)
    integration_id = db.Column(db.String(40), unique=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(150))
    icon = db.Column(db.String(150))
    channel = db.Column(db.String(150))
    token = db.Column(db.String(150))
    developer_id = db.Column(db.Integer, db.ForeignKey('developers.id'))


class Channel(db.Model):
    __tablename__ = 'channels'
    id = db.Column(db.Integer, primary_key=True)
    developer_id = db.Column(db.Integer, db.ForeignKey('developers.id'))
    channel = db.Column(db.String(150))

    def __repr__(self):
        return '<Channel %r>' % self.channel
