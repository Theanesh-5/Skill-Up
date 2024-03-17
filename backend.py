
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

users_db = {
    "user1@example.com": {"password": "password1"},
    "user2@example.com": {"password": "password2"},
}

groups_db = [
    {"id": 1, "name": "Python Study Group", "description": "Study Python programming language."},
    {"id": 2, "name": "Web Development Workshop", "description": "Learn web development concepts."},
    {"id": 3, "name": "Data Science Bootcamp", "description": "Join for hands-on data science projects."},
]

class User(BaseModel):
    email: str
    password: str

class Group(BaseModel):
    id: int
    name: str
    description: str

@app.post("/login")
def login(user: User):
    if user.email in users_db and users_db[user.email]["password"] == user.password:
        return {"message": "Login successful"}
    else:
        raise HTTPException(status_code=401, detail="Invalid credentials")

@app.get("/groups", response_model=List[Group])
def get_groups():
    return groups_db
