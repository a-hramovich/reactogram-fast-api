from fastapi import APIRouter, Depends, HTTPException
from starlette import status

from auth.oauth2 import get_current_user
from db.db import get_db
from db.db_comment import get_all_by_post_id, create_comment
from db.db_post import get_post
from routers.schemas import CommentBase, UserAuth

router = APIRouter(
    prefix='/comment',
    tags=['comment'],
)


@router.post('/create')
def create(request: CommentBase, db=Depends(get_db), user: UserAuth = Depends(get_current_user)):
    post = get_post(db, request.post_id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Post with id {request.post_id} not found')
    return create_comment(request, db, user)


@router.get('/all/{post_id}')
def get_all_comments(post_id: int, db=Depends(get_db)):
    return get_all_by_post_id(db, post_id)
