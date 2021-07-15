import datetime as dt
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, orm
from database.database import Base

class Client(Base):
    ''' Defining the Client table in our database '''
    __tablename__ = "client"
    id_client = Column(Integer, primary_key=True, index=True)
    name = Column(String(25))
    firstname = Column(String(25))
    information = Column(String(100))

    # Adding the relationship between our tables
    client_texts = orm.relationship("Text", back_populates="owner")


class Text(Base):
    ''' Defining the Text table in our database '''
    __tablename__ = "text"
    id_text = Column(Integer, primary_key=True, index=True)
    content = Column(String(255))
    feeling = Column(Integer)
    creation_date = Column(DateTime, default=dt.datetime.utcnow)
    modification_date = Column(DateTime, default=dt.datetime.utcnow)
    id_client = Column(Integer, ForeignKey("client.id_client"))

    # Adding the relationship between our tables
    owner = orm.relationship("Client", back_populates="client_texts")