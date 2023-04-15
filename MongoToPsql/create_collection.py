from pymongo import MongoClient
from bson import ObjectId

def create_and_insert_data(mongo_uri, db_name, collection_name, data):
    # create MongoDB client
    mongo_client = MongoClient(mongo_uri)

    # get database and collection
    mongo_db = mongo_client[db_name]
    mongo_collection = mongo_db[collection_name]

    # insert data into collection
    mongo_collection.insert_one(data)

    # close MongoDB connection
    mongo_client.close()

if __name__ == '__main__':
    # MongoDB Atlas connection settings
    mongo_uri = 'mongodb+srv:///<yourmongopasswd>:<yourmongouser>@cluster0.wiipzzr.mongodb.net/<yourmongodb>?retryWrites=true&w=majority'

    # define database and collection names
    db_name = '<yourmongodb>'
    collection_name = 'person'

    # define data to insert
    data = {
        "_id": ObjectId("609ddcee97d1c227b5fc6c32"),
        "name": "John Smith",
        "age": 35,
        "email": "john.smith@example.com",
        "address": {
            "street": "123 Main St",
            "city": "Anytown",
            "state": "CA",
            "zip": "12345"
        },
        "interests": ["hiking", "reading", "travel"]
    }

    # create and insert data into collection
    create_and_insert_data(mongo_uri, db_name, collection_name, data)
