import pymongo
import os

ME_CONFIG_MONGODB_URL = os.environ.get('ME_CONFIG_MONGODB_URL')

class MongoLibrary():
    client = pymongo.MongoClient(f"mongodb://{os.environ.get('MONGO_INITDB_ROOT_USERNAME', 'root')}:{os.environ.get('MONGO_INITDB_ROOT_PASSWORD', 'example')}@{os.environ.get('MONGO_HOST', 'localhost')}:27017/"
)
    database = client['crm_db']
    contacts_collection = database['contacts']
