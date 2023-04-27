import pymongo
import os

ME_CONFIG_MONGODB_URL = os.environ.get('ME_CONFIG_MONGODB_URL')

class MongoLibrary():
    client = pymongo.MongoClient(f'{ME_CONFIG_MONGODB_URL}, localhost:27017')
    database = client['crm_db']
    contacts_collection = database['contacts']
