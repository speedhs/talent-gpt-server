from mongoengine import StringField, ListField, DictField, ReferenceField
from .base import BaseDocument

class Message(BaseDocument):
    meta = {'collection': 'messages'}
    
    role = StringField(required=True, choices=['user', 'assistant'])
    content = StringField(required=True)
    metadata = DictField()

class ChatSession(BaseDocument):
    meta = {'collection': 'chat_sessions'}
    
    recruiter_id = StringField(required=True)
    session_type = StringField(required=True)
    initial_context = StringField()
    messages = ListField(ReferenceField(Message))
    status = StringField(default='active', choices=['active', 'completed'])
    metadata = DictField()

    class Config:
        schema_extra = {
            "example": {
                "recruiter_id": "123",
                "session_type": "candidate_search",
                "initial_context": "Looking for Python developers",
                "messages": [
                    {
                        "role": "user",
                        "content": "Find candidates with 5+ years of Python experience",
                        "metadata": {"query_type": "experience"}
                    }
                ],
                "status": "active",
                "metadata": {"search_criteria": {"experience": "5+", "language": "Python"}}
            }
        } 