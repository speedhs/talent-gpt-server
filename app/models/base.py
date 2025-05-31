from datetime import datetime
from mongoengine import Document, StringField, DateTimeField, ObjectIdField
from mongoengine.fields import DictField, ListField, ReferenceField

class BaseDocument(Document):
    meta = {'abstract': True}
    
    created_at = DateTimeField(default=datetime.utcnow)
    updated_at = DateTimeField(default=datetime.utcnow)

    def save(self, *args, **kwargs):
        self.updated_at = datetime.utcnow()
        return super().save(*args, **kwargs) 