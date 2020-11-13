# -*- mode: python -*- -*- coding: utf-8 -*-
from pydantic import BaseModel

class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str

    class Config:
        orm_mode = True

class User(BaseModel):
    name: str

    class Config:
        orm_mode = True
