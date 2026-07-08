from sqlalchemy import create_engine

# import sessionmaker
from sqlalchemy.orm import sessionmaker

# import declarative_base
from sqlalchemy.ext.declarative import declarative_base

# copy this from neon dashboard and replace the username,password,and host with your own credentials
# DATABASE_URL = "postgresql://username:password@host:port/database_name?sslmode=require&channel_binding=require"

import os           
# import function that can read the .env file ,i.e open the .env file and load all the environment variables from it into the memory

from dotenv import load_dotenv
# load environment variables from .env file
load_dotenv()
# get the database url from the .env file
DATABASE_URL = os.getenv("DATABASE_URL")  


# here,we create a connection to the postgreSQL database hosted on the cloud(neon)
# note click "show password" and copy the complete connection string

# create SQLAlchemy engine
# the engine is responsible for connecting FASTapi with the cloud PostgreSQL
engine= create_engine(DATABASE_URL)

sessionLocal = sessionmaker(bind=engine)

# base class as all databse tables will inherit from this class

Base = declarative_base()

# dependency function to get the database session,function provides a database whenever an api requires datbase access
def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()