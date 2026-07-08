from sqlalchemy import create_engine

# import sessionmaker
from sqlalchemy.orm import sessionmaker

# import declarative_base
from sqlalchemy.ext.declarative import declarative_base

# copy this from neon dashboard and replace the username,password,and host with your own credentials
# DATABASE_URL = "postgresql://username:password@host:port/database_name?sslmode=require&channel_binding=require"

DATABASE_URL ="postgresql://neondb_owner:npg_yGDl1azib0UJ@ep-summer-fire-aoz1iz4u-pooler.c-2.ap-southeast-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require"
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