from sqlalchemy.orm import Session
from . import schema, database


def save_device_info(db: Session, info: schema.Users):
    device_info_model = database.Users(**info.dict())
    db.add(device_info_model)
    db.commit()
    db.refresh(device_info_model)
    return device_info_model

def get_device_info(db: Session, token: str = None):
    if token is None:
        return db.query(database.Users).all()
    else:
        return db.query(database.Users).filter(database.Users.token == token).first()

def save_configuration(db: Session, config: schema.Items):
    config_model = database.Items(**config.dict())
    db.add(config_model)
    db.commit()
    db.refresh(config_model)
    return config_model

def get_configuration(db: Session):
    return db.query(database.Items).all()

def delete_configuration(db: Session):
    db.query(database.Items).delete()

def error_message(message):
    return {
        'error': message
    }