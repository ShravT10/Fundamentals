'''
Response model basically hides data which should not be seen to the public
'''

from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()

class UserInDB(BaseModel):
    username: str
    password: str
    email: EmailStr
    is_active: bool = True


class UserShow(BaseModel):
    username: str
    email: EmailStr

@app.post('/add-user/',response_model=UserShow)
async def add_user(user: UserInDB):
    return user
