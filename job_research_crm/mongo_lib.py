import pymongo

class MongoLibrary():
    client = pymongo.MongoClient('mongodb://root:example@127.0.0.1:27017')
    database = client['crm_db']
    contacts_collection = database['contacts']
