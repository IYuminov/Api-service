from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, String, Boolean, Integer
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("postgresql://username:password@db:5432/nudges")
Session = sessionmaker(bind=engine)
Base = declarative_base()

class Users(Base):
    __tablename__ = 'Users'
    token = Column(String, primary_key = True)
    username = Column(String, default = 'user')

class Items(Base):
    __tablename__ = 'Items'
    id = Column(Integer, primary_key = True, autoincrement = True)
    models = Column(String)
    year = Column(Integer)
    was_accident = Column(Boolean)

Base.metadata.create_all(bind=engine)


with Session(autoflush=False, bind=engine) as db:
    item1 = Items(id=1, models='something', year=2010, was_accident=True)
    item2 = Items(id=2, models='Something', year=2011, was_accident=False)
    item3 = Items(id=3, models='SOMETHING', year=2012, was_accident=True)
    db.add_all([item1, item2, item3])
    db.commit()
