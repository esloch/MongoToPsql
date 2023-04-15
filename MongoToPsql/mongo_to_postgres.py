from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.dialects.postgresql import JSON
from pymongo import MongoClient
from bson import json_util


# MongoDB Atlas connection settings
mongo_uri = 'mongodb+srv://<yourmongopasswd>:<yourmongouser>@cluster0.wiipzzr.mongodb.net/<yourmongodb>?appName=mongosh+1.8.'

# create MongoDB client
mongo_client = MongoClient(mongo_uri)

# get database and collection
mongo_db = mongo_client['<yourmongodb>']
mongo_collection = mongo_db['<yourmongocollection>']

# PostgreSQL connection settings
postgres_uri = 'postgresql://<user>:<password>@localhost:5432/<dbname>'

# create SQLAlchemy engine
engine = create_engine(postgres_uri)

# create SQLAlchemy base class
Base = declarative_base()

# define PostgreSQL table schema
class MyTable(Base):
    __tablename__ = '<yourmongocollection>'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    email = Column(String)
    address = Column(JSON)
    interests = Column(JSON)

# create the table in PostgreSQL
Base.metadata.create_all(engine)

# create a session to interact with PostgreSQL
Session = sessionmaker(bind=engine)
session = Session()

# print data from collection
try:
    for doc in mongo_collection.find():
        # use json_util to serialize ObjectId values
        print(json_util.dumps(doc, indent=4))
except Exception as e:
    print(f"Error: {e}")

# iterate over documents in MongoDB collection
for doc in mongo_collection.find():
    try:
        row = MyTable(
            name=doc['name'],
            age=doc['age'],
            email=doc['email'],
            address=doc['address'],
            interests=doc['interests']
        )
        session.add(row)
        session.commit()
    except Exception as e:
        print(f"Error inserting data into PostgreSQL: {e}")
        session.rollback()

# close MongoDB connection and session
mongo_client.close()
session.close()


# MongoDB connection settings
# mongo_uri = 'mongodb://localhost:27017'
# mongo_db = 'my_mongo_db'
# mongo_collection = '<yourmongocollection>'
# connect to MongoDB and get the collection
# mongo_client = MongoClient(mongo_uri)
# mongo_collection = mongo_client[mongo_db][mongo_collection]

