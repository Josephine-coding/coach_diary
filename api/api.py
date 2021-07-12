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
def read_user(id_client: int, db: Session = Depends(get_db)):
    db_user = crud.get_client_by_id(db, id_client=id_client)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Client not found")
    return db_user

@app.get("/clients/{name}", response_model=schemas.Client)
#Get one client by providing a name
def read_username(name: str, db: Session = Depends(get_db)):
    db_user = crud.get_client_by_name(db, name=name)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Client not found")
    return db_user

@app.get("/clients/", response_model=List[schemas.Client])
#Get a list of all clients
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_all_clients(db, skip=skip, limit=limit)
    return users



##### TEXT REQUESTS #####

@app.get("/texts/{id_text}", response_model=schemas.Text)
# Get one text by providing id_text
def read_text(id_text: int, db: Session = Depends(get_db)):
    db_text = crud.get_text(db, id_text=id_text)
    if db_text is None:
        raise HTTPException(status_code=404, detail="Client not found")
    return db_text

