# MongoToPsql

This project contains utilities for working with PostgreSQL and MongoDB databases using Python. It includes scripts for creating a new user and database in PostgreSQL, importing data from MongoDB into PostgreSQL, and printing data from a MongoDB collection in pretty JSON format.

# Installation
Before using the scripts in this project, you will need to install the following dependencies: 
- psycopg2: PostgreSQL adapter for Python 
- pymongo: MongoDB driver for Python 
- sqlalchemy: SQL toolkit and ORM for Python 
You can install these packages using pip: 
```pip install psycopg2 pymongo sqlalchemy``` 
# Usage 
## Creating a PostgreSQL user and database 
To create a new user and database in PostgreSQL, you can use the create_user_and_database function in the postgresql_utils module. This function takes three arguments: user, password, and database. To run this function from the command line, navigate to the project directory and run the following command:  

```python postgresql_utils.py create_user_and_database <user> <password> <database>```  

Replace *<user>*, *<password>*, and *<database>* with the desired values. 

## Importing data from MongoDB into PostgreSQL 
To import data from a MongoDB collection into a PostgreSQL table using the mongo_to_postgres module, you will need to provide your MongoDB and PostgreSQL credentials as arguments. The import_mongo_to_postgres function takes four arguments: mongo_uri, postgres_uri, mongo_db, and mongo_collection. You can then call this function from the command line using the following command:

Be sure to replace <mongo_uri>, <postgres_uri>, <mongo_db>, and <mongo_collection> with your actual credentials.

```python mongo_to_postgres.py``` 

This project provides useful utilities for working with PostgreSQL and MongoDB databases using Python. The postgresql_utils module allows you to create a new user and database in PostgreSQL, while the mongo_to_postgres module allows you to import data from a MongoDB collection into a PostgreSQL table. The mongo_utils module provides a function for printing data from a MongoDB collection in pretty JSON format.
