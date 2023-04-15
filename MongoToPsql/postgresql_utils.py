import sys
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

def create_user_and_database(user, password, dbname):
    # define PostgreSQL connection settings
    pg_user = 'postgres'
    pg_password = 'postgres'
    pg_host = 'localhost'
    pg_port = 5432

    # create a PostgreSQL superuser
    engine = create_engine(f'postgresql://{pg_user}:{pg_password}@{pg_host}:{pg_port}/postgres')
    conn = engine.connect()
    conn.execute(f"CREATE USER {user} WITH PASSWORD '{password}';")
    conn.execute(f"ALTER USER {user} CREATEDB;")
    conn.close()

    # create the database with the new user as the owner
    engine = create_engine(f'postgresql://{user}:{password}@{pg_host}:{pg_port}/{dbname}')
    if not database_exists(engine.url):
        create_database(engine.url)
    print(f"Database {dbname} and user {user} created successfully!")

if __name__ == '__main__':
    # get arguments from command line
    user = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    # call create_user_and_database() function
    create_user_and_database(user, password, dbname)
