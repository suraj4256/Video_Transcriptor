from bson import ObjectId
from schematics.models import Model
from datetime import datetime
from schematics.types import StringType, DateTimeType, EmailType, IntType

class User(Model):
    id = ObjectId()
    name = StringType(required=True)
    email = EmailType(required=True)
    password = StringType(required=True)
    age = int 
    created_at = DateTimeType(default=datetime.utcnow)

