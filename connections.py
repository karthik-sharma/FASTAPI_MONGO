from pymongo.mongo_client import MongoClient


client = MongoClient('mongodb://localhost:27017')
db = client["customers"]
collections = db["customer_data"]

