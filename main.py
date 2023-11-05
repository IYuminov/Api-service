from enum import Enum
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class DogType(str, Enum):
    terrier = "terrier"
    bulldog = "bulldog"
    dalmatian = "dalmatian"


class Dog(BaseModel):
    name: str
    pk: int
    kind: DogType


class Timestamp(BaseModel):
    id: int
    timestamp: int


dogs_db = {
    0: Dog(name='Bob', pk=0, kind='terrier'),
    1: Dog(name='Marli', pk=1, kind="bulldog"),
    2: Dog(name='Snoopy', pk=2, kind='dalmatian'),
    3: Dog(name='Rex', pk=3, kind='dalmatian'),
    4: Dog(name='Pongo', pk=4, kind='dalmatian'),
    5: Dog(name='Tillman', pk=5, kind='bulldog'),
    6: Dog(name='Uga', pk=6, kind='bulldog')
}


post_db = [
    Timestamp(id=0, timestamp=12),
    Timestamp(id=1, timestamp=10)
]


# Root
@app.get('/')
async def root() -> str:
    return 'Welcome our clinic!'


# Get Post
@app.post("/post")
async def post() -> dict:
    add_data_timestamp = Timestamp(id=len(post_db), timestamp=round(time.time()))
    post_db.append(add_data_timestamp)
    return add_data_timestamp


# Get all Dogs
@app.get("/dogs")
async def get() -> dict:
    return dogs_db



# Get Dogs by type
@app.get("/dog")
async def get(kind: str) -> list:
    result = []
    for i in dogs_db.values():
        if i.kind == DogType(kind):
            result.append(i)
    return result


# Create Dog
@app.post("/dog")
async def post(name_dog: str, kind_dog: str) -> dict:
    add_dog = Dog(name= name_dog, pk= len(dogs_db), kind= DogType(kind_dog))
    dogs_db[len(dogs_db)] = add_dog
    return add_dog



# Get Dog By Pk
# решение годится, если pk уникальный
@app.get("/dog/{pk}")
async def get(pk: str) -> dict:
    for i in dogs_db.values():
        if i.pk == int(pk):
            return i



# Update Dog by pk
@app.patch("/dog/{old_pk}")
async def patch(new_name: str, old_pk: str, new_kind: str) -> dict:
    for i in range(len(dogs_db)):
        if dogs_db[i].pk == int(old_pk):
            dogs_db[i].name = new_name
            dogs_db[i].kind = DogType(new_kind)
            return dogs_db[i]