from mongoengine import StringField, FloatField, ListField, DictField, EmailField, EmbeddedDocument, EmbeddedDocumentField
from .base import BaseDocument

class Skill(EmbeddedDocument):
    name = StringField(required=True)
    years_experience = FloatField(required=True, min_value=0)
    level = StringField(required=True, choices=['beginner', 'intermediate', 'expert'])

class Candidate(BaseDocument):
    meta = {'collection': 'candidates'}
    
    name = StringField(required=True, max_length=100)
    email = EmailField(required=True, unique=True)
    phone = StringField()
    skills = ListField(EmbeddedDocumentField(Skill), required=True)
    experience_years = FloatField(required=True, min_value=0)
    current_role = StringField(max_length=100)
    current_company = StringField(max_length=100)
    location = StringField(required=True, max_length=100)
    availability = StringField(required=True)
    match_score = FloatField(min_value=0, max_value=1)
    details = DictField()

    class Config:
        schema_extra = {
            "example": {
                "name": "Jane Smith",
                "email": "jane.smith@example.com",
                "phone": "+1234567890",
                "skills": [
                    {
                        "name": "Python",
                        "years_experience": 5.5,
                        "level": "expert"
                    },
                    {
                        "name": "React",
                        "years_experience": 3.0,
                        "level": "intermediate"
                    }
                ],
                "experience_years": 7.5,
                "current_role": "Senior Software Engineer",
                "current_company": "Tech Solutions Inc",
                "location": "New York, NY",
                "availability": "Available in 2 weeks",
                "match_score": 0.95,
                "details": {
                    "education": "MS in Computer Science",
                    "languages": ["English", "Spanish"],
                    "preferred_roles": ["Backend Developer", "Tech Lead"]
                }
            }
        } 