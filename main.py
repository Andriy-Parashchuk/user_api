from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel, Field

app = FastAPI()


class User(BaseModel):
    id: int
    username: str
    email: str


users = [
    {'id': 1, 'username': 'harosh', 'email': 'hehe@gmail.com'}
]


@app.get('/users')
def get_all_users():
    return users


@app.post('/users/new')
def create_user(user: User):
    users.append(user)
    return user


@app.get('/users/{user_id}')
def get_user_by_id(user_id:int):
    for user in users:
        if user['id'] == user_id:
            return user
    return 'nema'

