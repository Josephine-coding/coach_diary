from sqlalchemy.orm import Session

from database import models, schemas

def get_client_by_id(db:Session, id_client:int):
    ''' Query to get one client by providing its id '''
    return db.query(models.Client).filter(models.Client.id_client==id_client).first

def get_client_by_name(db:Session, name:str):
    ''' Query to get one client by providing its name '''
    return db.query(models.Client).filter(models.Client.name==name).first

def get_all_clients(db: Session, skip: int = 0, limit: int = 100):
    ''' Query to get a list of all clients '''
    return db.query(models.Client).offset(skip).limit(limit).all()

