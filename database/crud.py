from sqlalchemy.orm import Session
from datetime import datetime

from database import models, schemas

##### CLIENT REQUESTS #####

def get_client_by_id(db:Session, id_client:int):
    ''' Query to get one client by providing its id '''
    return db.query(models.Client).filter(models.Client.id_client==id_client).first


def get_client_by_name(db:Session, name:str):
    ''' Query to get one client by providing its name '''
    return db.query(models.Client).filter(models.Client.name==name).first


def get_all_clients(db: Session, skip: int = 0, limit: int = 100):
    ''' Query to get a list of all clients '''
    return db.query(models.Client).offset(skip).limit(limit).all()


def create_client(db: Session, client):
    ''' Query to create a client '''
    new_client = models.Client(
        name=client['name'],
        firstname=client['firstname'],
        information=client['information'],
        creation_date=datetime.today().strftime('%Y-%m-%d')
    )
    db.add(new_client)
    db.commit()
    db.refresh(new_client)
    return new_client


def delete_client_by_id(db: Session, id: int):
    ''' Query to delete a client by providing its id '''
    client_to_delete = db.query(models.Client).filter(models.Client.id_customer == id).first()
    db.delete(client_to_delete)
    db.commit()
    return "Successfully deleted"


def update_client_by_id(db: Session, id: int, updated_client: dict):
    ''' Query to update a client by providing its id '''
    client_to_update = db.query(models.Client).filter(models.Client.id_customer == id).first()
    client_to_update.name = updated_client['name']
    client_to_update.firstname = updated_client['firstname']
    client_to_update.information = updated_client['information']
    client_to_update.modification_date = updated_client['modification_date']
    db.commit()
    db.refresh(client_to_update)
    return "Successfully updated!"


##### TEXT REQUESTS #####

def create_text(db: Session, new_text: dict):
    ''' Query to create a text '''
    text = models.Text(
        content=new_text['content'],
        creation_date=new_text['creation_date'],
        first_feeling=new_text['first_feeling '],
        first_pourcentage=new_text['first_pourcentage'],
        second_feeling=new_text['second_feeling'],
        second_pourcentage=new_text['second_pourcentage'],
        third_feeling=new_text['third_feeling'],
        third_pourcentage=new_text['third_pourcentage'],
        id_customer=new_text['id_customer']
    )
    db.add(text)
    db.commit()
    return text


def get_text(db, id_text: int):
    ''' Query to get one text by providing its id '''
    return db.get(models.Text, id_text)


def get_all_text(id: int,db: Session, skip: int = 0, limit: int = 100):
    ''' Query to get a list of all texts '''
    return db.query(models.Text).filter(models.Text.id_customer == id).offset(skip).limit(limit).all()


def delete_text(db: Session, text_to_delete: models.Text):
    ''' Query to delete a text '''
    db.delete(text_to_delete)
    db.commit()
    return "Successfully deleted"