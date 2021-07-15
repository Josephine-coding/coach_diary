from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from typing import List

import sys
sys.path.insert(0, "/home/apprenant/PycharmProjects/coach_diary")

from database import crud, models, schemas
from database.database import SessionLocal, engine

# Creating the models
models.Base.metadata.create_all(bind=engine)

# Creating the api
app = FastAPI()

# welcome page
@app.get('/')
async def hello():
    return {"Welcome":"Here"}

# Connection to db
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


##### CLIENT REQUESTS #####

@app.get("/clients/{id_client}", response_model=schemas.Client)
# Get one client by providing id_client
def read_user(id_client: int, db= Depends(get_db)):
    db_user = crud.get_client_by_id(db, id_client=id_client)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Client not found")
    return db_user

@app.get("/clients/{name}", response_model=schemas.Client)
# Get one client by providing a name
def read_username(name: str, db: Session = Depends(get_db)):
    db_user = crud.get_client_by_name(db, name=name)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Client not found")
    return db_user

@app.get("/clients/", response_model=List[schemas.Client])
# Get a list of all clients
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_all_clients(db, skip=skip, limit=limit)
    return users

@app.post("/clients/", response_model=schemas.Client)
# Create a new client
def create_user(new_cust: dict, db: Session = Depends(get_db)):
    cust = crud.get_client_by_name(db=db, name=new_cust['name'])
    if cust:
        raise HTTPException(status_code=400, detail="User already registered")
    return crud.create_client(db=db, client=new_cust)

@app.put("/clients/{id_client}")
# Update a client providing its id
def update_user_by_id(id_client: int, updated_cust: dict, db: Session = Depends(get_db)):
    return  crud.update_client_by_id(db=db, id=id_client, updated_client=updated_cust)

@app.delete("/clients/{id_client}")
#Delete a client providing its id
def delete_user_by_id(id_client: int, db: Session = Depends(get_db)):
    return crud.delete_client_by_id(db=db, id=id_client)


##### TEXT REQUESTS #####

@app.get("/texts/{id_text}", response_model=schemas.Text)
# Get one text by providing id_text
def read_text(id_text: int, db: Session = Depends(get_db)):
    db_text = crud.get_text(db, id_text=id_text)
    if db_text is None:
        raise HTTPException(status_code=404, detail="Text not found")
    return db_text


@app.get("/texts/{id_client}", response_model=List[schemas.Text])
# Get all texts for one client
def read_texts_for_one_client(id_client: int, db: Session = Depends(get_db), skip=0, limit=100):
    db_text = crud.get_all_texts_for_one_client(db, id_client=id_client, skip=skip, limit= limit)
    if db_text is None:
        raise HTTPException(status_code=404, detail="Text not found")
    return db_text


@app.get("/texts/", response_model=List[schemas.Text])
# Get a list of all texts
def read_texts(skip: int = 0, limit: int = 100, db:Session = Depends(get_db)):
    texts = crud.get_all_texts(db, skip=skip, limit=limit)
    return texts


@app.post("/texts/", response_model=schemas.Text)
# Create a new text
def create_new_text(new_text: dict, db: Session = Depends(get_db)):
    text = crud.create_text(db, new_text)
    return text

@app.delete("/texts/{id_text}")
# Delete a text providing its id
def delete_text_by_id(id_text:int, db: Session = Depends(get_db)):
    return crud.delete_text(db, id_text)