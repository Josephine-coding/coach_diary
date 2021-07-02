from pydantic import BaseModel
from typing import Optional, List
import datetime as dt

## Creating the pydantic schemas for Text

class TextBase(BaseModel):
    content: str

class TextCreate(TextBase):
    pass

class Text(TextBase):
    id_text: int
    id_client: int
    feeling: str
    creation_date: dt.datetime
    modification_date: Optional[dt.datetime] = None

    class Config:
        orm_mode = True


## Creating the pydantic schemas for Client

class ClientBase(BaseModel):
    name: str

class ClientCreate(ClientBase):
    firstname: str
    info: Optional[str] = "Pas d'informations"

class Client(ClientBase):
    id_client: int
    firstname: str
    info: Optional[str] = "Pas d'informations"
    texts: List[Text] = []

    class Config:
        orm_mode = True