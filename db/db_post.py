import datetime

from fastapi import HTTPException
from sqlalchemy.orm import Session
from starlette import status

from db.models import DBPost
from routers.schemas import PostBase


def create(request: PostBase, db: Session, user_id: int):
    new_post = DBPost(
        image_url=request.image_url,
        image_url_type=request.image_url_type,
        caption=request.caption,
        timestamp=datetime.datetime.now(),
        user_id=user_id
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


def get_all(db: Session):
    return db.query(DBPost).all()


def get_post(db: Session, post_id: int):
    return db.query(DBPost).filter(DBPost.id == post_id).first()


def delete(post_id: int, db: Session, user_id: int):
    post = get_post(db, post_id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Post with id {post_id} not found')
    if post.user_id != user_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail='Only post creator can delete post')
    db.delete(post)
    db.commit()
    return 'ok'
