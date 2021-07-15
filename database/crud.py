from sqlalchemy.orm import Session
from datetime import datetime

from database import models, schemas

##### CLIENT REQUESTS #####

def get_client_by_id(db:Session, id_client:int):
    ''' Query to get one client by providing its id '''
    return db.query(models.Client).filter(models.Client.id_client == id_client).first()


def get_client_by_name(db:Session, name:str):
    ''' Query to get one client by providing its name '''
    return db.query(models.Client).filter(models.Client.name == name).first()


def get_all_clients(db:Session, skip: int = 0, limit: int = 100):
    ''' Query to get a list of all clients '''
    return db.query(models.Client).offset(skip).limit(limit).all()


def create_client(db:Session, client):
    ''' Query to create a client '''
    new_client = models.Client(
        name=client['name'],
        firstname=client['firstname'],
        information=client['information'],
        #creation_date=datetime.today().strftime('%Y-%m-%d')
    )
    db.add(new_client)
    db.commit()
    db.refresh(new_client)
    return new_client


def delete_client_by_id(db:Session, id:int):
    ''' Query to delete a client by providing its id '''
    client_to_delete = db.query(models.Client).filter(models.Client.id_client == id).first()
    db.delete(client_to_delete)
    db.commit()
    return "Successfully deleted"


def update_client_by_id(db:Session, id:int, updated_client:dict):
    ''' Query to update a client by providing its id '''
    client_to_update = db.query(models.Client).filter(models.Client.id_client == id).first()
    client_to_update.name = updated_client['name']
    client_to_update.firstname = updated_client['firstname']
    client_to_update.information = updated_client['information']
    client_to_update.modification_date = updated_client['modification_date']
    db.commit()
    db.refresh(client_to_update)
    return "Successfully updated!"


##### TEXT REQUESTS #####

def create_text(db: Session, new_text:dict):
    ''' Query to create a text '''
    text = models.Text(
        content=new_text['content'],
        feeling=new_text['feeling '],
        creation_date=datetime.today().strftime('%Y-%m-%d'),
        id_client=new_text['id_client']
    )
    db.add(text)
    db.commit()
    return text


def get_text(db:Session, id_text:int):
    ''' Query to get one text by providing its id '''
    return db.get(models.Text).filter(models.Text.id_text == id_text).first()


def get_all_texts_for_one_client(db:Session, id_client:int, skip: int = 0, limit: int = 100):
    ''' Query to get a list of all texts for one client '''
    return db.query(models.Text).filter(models.Text.id_client == id_client).offset(skip).limit(limit).all()


def get_all_texts(db:Session, skip: int = 0, limit: int = 100):
    ''' Query to get a list of all texts '''
    return db.query(models.Text).offset(skip).limit(limit).all()


def delete_text(db:Session, id_text:int):
    ''' Query to delete a text '''
    text_to_delete = db.query(models.Text).filter(models.Text.id_text == id_text).first()
    db.delete(text_to_delete)
    db.commit()
    return "Successfully deleted"