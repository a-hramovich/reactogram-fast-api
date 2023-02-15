from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.sql.functions import current_user

from auth.oauth2 import get_current_user
from db import db_post
from db.db import get_db
from db.db_post import create, get_all
from routers.schemas import PostDisplay, PostBase, UserAuth

router = APIRouter(
    prefix='/post',
    tags=['post'],
)


@router.post('', response_model=PostDisplay)
def create_new_post(request: PostBase, db=Depends(get_db), user: UserAuth = Depends(get_current_user)):
    return create(request, db, user.id)


@router.get('/all', response_model=List[PostDisplay])
def get_all_posts(db=Depends(get_db)):
    return get_all(db)


@router.delete('/{id}')
def delete_post(id: int, db=Depends(get_db), user: UserAuth = Depends(get_current_user)):
    return db_post.delete(id, db, user.id)
