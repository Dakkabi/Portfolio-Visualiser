from pydantic import BaseModel


class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class UserUpdate(UserCreate):
    pass

class UserSchema(UserBase):
    id: int