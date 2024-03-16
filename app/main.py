from fastapi import FastAPI, Depends, HTTPException
from .database import Session
from .schema import Users, Items
from . import functions

app = FastAPI()

def db():
    try:
        db = Session()
        yield db
    finally:
        db.close()

@app.get('/health')
def get() -> dict:
    return {'status': 'OK'}

@app.get('/')
def root() -> str:
    return 'Welcome to service!'

@app.post('/users')
def save_device_info(info: Users, db=Depends(db)):
    object_in_db = functions.get_device_info(db, info.token)
    if object_in_db:
        raise HTTPException(400, detail= functions.error_message('This info already exists'))
    return functions.save_device_info(db,info)

@app.get('/user/{token}')
def get_device_info(token: str, db=Depends(db)):
    info = functions.get_device_info(db,token)
    if info:
        return info
    else:
        raise HTTPException(404, functions.error_message(f'No user found for token {token}'))

@app.get('/users')
def get_all_device_info(db=Depends(db)):
    return functions.get_device_info(db)

@app.post('/items')
def save_configuration(config: Items, db=Depends(db)):
    functions.delete_configuration(db)
    return functions.save_configuration(db, config)

@app.get('/items')
def get_configuration(db=Depends(db)):
    config = functions.get_configuration(db)
    if config:
        return config
    else:
        raise HTTPException(404, functions.error_message('No items set'))
