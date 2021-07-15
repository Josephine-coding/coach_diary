import pytest
import asyncio
import sys
sys.path.insert(0, "/home/apprenant/PycharmProjects/coach_diary")
from api.api import models
from api.api import get_db
#from src.utils.mysql_utils import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

test_database_name = 'coach_diary'


@pytest.fixture(scope="module")
def event_loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()


@pytest.mark.asyncio
@pytest.fixture(scope='module')
def session_make():
    db = get_db()
    yield db


@pytest.mark.asyncio
@pytest.fixture(scope='module')
def init_db(event_loop, session_make):
    db_connection = get_db()
    models.Base.metadata.create_all(bind=db_connection)

    populate_table = """
    INSERT INTO customer(name,firstname, information)
    VALUES("doe","jane", "test info")
    """
    cursor.execute(populate_table)
    session_make.commit()

    yield cursor