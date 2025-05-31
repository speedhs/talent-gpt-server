from mongoengine import StringField, ListField
from .base import BaseDocument

class Company(BaseDocument):
    meta = {'collection': 'companies'}
    
    name = StringField(required=True, max_length=100, unique=True)
    industry = StringField(required=True, max_length=50)
    size = StringField(required=True, max_length=50)
    location = StringField(required=True, max_length=100)
    description = StringField(required=True, max_length=1000)
    tech_stack = ListField(StringField(), required=True)
    benefits = ListField(StringField())
    culture = StringField(max_length=500)

    class Config:
        schema_extra = {
            "example": {
                "name": "Tech Corp",
                "industry": "Technology",
                "size": "500-1000",
                "location": "San Francisco, CA",
                "description": "Leading technology company specializing in AI solutions",
                "tech_stack": ["Python", "React", "AWS", "Docker"],
                "benefits": ["Health Insurance", "401k", "Remote Work"],
                "culture": "Innovative and collaborative environment"
            }
        } 