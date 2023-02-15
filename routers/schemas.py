from datetime import datetime
from enum import Enum
from typing import List

from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    email: str
    password: str


class UserDisplay(BaseModel):
    username: str
    email: str
    id: int

    class Config:
        orm_mode = True


class User(BaseModel):
    username: str

    class Config:
        orm_mode = True


class PostBase(BaseModel):
    image_url: str
    image_url_type: str
    caption: str


class ImageUrlType(str, Enum):
    relative = 'relative'
    absolute = 'absolute'


class CommentDisplay(BaseModel):
    text: str
    username: str
    timestamp: datetime

    class Config:
        orm_mode = True


class PostDisplay(BaseModel):
    id: int
    image_url: str
    image_url_type: ImageUrlType
    caption: str
    timestamp: datetime
    user: User
    comments: List[CommentDisplay]

    class Config:
        orm_mode = True


class UserAuth(BaseModel):
    id: int
    username: str
    email: str


class CommentBase(BaseModel):
    text: str
    post_id: int
