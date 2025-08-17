from pymongo import MongoClient
import settings

client = MongoClient(settings.mongodb_uri, settings.port)
print("Connected to MongoDB")

db = client['VideoStreamingDB']