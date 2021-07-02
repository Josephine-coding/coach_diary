from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from conf.conf_connect import mysql_pseudo, mysql_pw

# Defining the database name
DATABASE_NAME = 'coach_diary'

# Creating the engine to ensure db connection
engine = create_engine('mysql+mysqlconnector://{0}:{1}@localhost/{2}'.format(mysql_pseudo, mysql_pw, DATABASE_NAME))

# Getting a declarative base to use in models
Base = declarative_base()

# Creating a Session to make db connection
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)