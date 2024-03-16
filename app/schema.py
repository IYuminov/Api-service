from pydantic import BaseModel
from typing import Optional

class Users(BaseModel):
    token: str
    username: Optional[str]

    class Config:
        orm_mode = True

class Items(BaseModel):
    models: str
    year: int
    was_accident: bool

    class Config:
        orm_mode = True