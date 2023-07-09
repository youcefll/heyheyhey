from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from . import db
from flask_login import UserMixin


class MembershipLevel(db.Model):
    __tablename__ = 'membership_levels'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    price = Column(Integer)
    benefits = Column(String)
    duration = Column(String)



class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(120))




class Member(db.Model):
    __tablename__ = 'members'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(String)
    membership_level_id = Column(Integer, ForeignKey('membership_levels.id'))
    membership_level = relationship('MembershipLevel')
    profile_picture = Column(String)
    biography = Column(String)
    # Add other member fields as needed


class PaymentInformation(db.Model):
    __tablename__ = 'payment_information'
    id = Column(Integer, primary_key=True)
    member_id = Column(Integer, ForeignKey('members.id'))
    member = relationship('Member')
    payment_details = Column(String)
    expiry_date = Column(String)
    payment_method = Column(String)
    billing_address = Column(String)
    status = Column(String)
    # Add other payment information fields as needed


class Preference(db.Model):
    __tablename__ = 'preferences'
    id = Column(Integer, primary_key=True)
    member_id = Column(Integer, ForeignKey('members.id'))
    member = relationship('Member')
    preferences = Column(String)
    theme = Column(String)
    language = Column(String)
    notification_preferences = Column(String)
    # Add other preference fields as needed


# Add other tables as needed
