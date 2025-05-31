from mongoengine import StringField, IntField, ListField, EmailField
from .base import BaseDocument

class RecruiterProfile(BaseDocument):
    meta = {'collection': 'recruiter_profiles'}
    
    name = StringField(required=True, max_length=100)
    email = EmailField(required=True, unique=True)
    company = StringField(required=True, max_length=100)
    position = StringField(required=True, max_length=100)
    experience_years = IntField(required=True, min_value=0)
    specialties = ListField(StringField(), required=True)
    bio = StringField(max_length=500) 