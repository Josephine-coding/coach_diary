from api import api
from typing import List
from fastapi import Depends
import api.schemas as schemas
from api.api import get_db, read_users


# def test_api_get_cust_by_name(session_make):
#     response = api.read_username("doe", session_make)
#     assert isinstance(response, model.Customer)
#
#
#
#
# def test_api_get_cust_by_id(session_make):
#     response = api.read_user(1, session_make)
#     assert isinstance(response, model.Customer)

def test_api_get_all_clients(Depends(get_db)):
    response = read_users(skip= 0, limit= 100, db= Depends(get_db))
    assert isinstance(response, List[schemas.Client])