import random
import string
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, String, Boolean, Integer
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("postgresql://username:password@db:5432/db-service")
Session = sessionmaker(bind=engine)
Base = declarative_base()

class Users(Base):
    __tablename__ = 'Users'
    token = Column(String, primary_key=True)
    username = Column(String, default='user')

class Items(Base):
    __tablename__ = 'Items'
    id = Column(Integer, primary_key=True, index=True)
    models = Column(String)
    year = Column(Integer)
    was_accident = Column(Boolean)

Base.metadata.create_all(bind=engine)

def generate_random_string(length):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string

with Session(autoflush=False, bind=engine) as db:
    item1 = Items(models='something', year=2010, was_accident=True)
    item2 = Items(models='Something', year=2011, was_accident=False)
    item3 = Items(models='SOMETHING', year=2012, was_accident=True)
    db.add_all([item1, item2, item3])
    db.commit()

with Session(autoflush=False, bind=engine) as db:
    item1 = Users(token=generate_random_string(10), username='Tim')
    item2 = Users(token=generate_random_string(10), username='Rob')
    item3 = Users(token=generate_random_string(10), username='Bob')
    db.add_all([item1, item2, item3])
    db.commit()
