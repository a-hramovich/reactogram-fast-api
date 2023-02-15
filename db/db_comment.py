import datetime

from sqlalchemy.orm import Session

from db.models import DBComment
from routers.schemas import CommentBase, UserAuth


def get_all_by_post_id(connection: Session, post_id):
    return connection.query(DBComment).filter(DBComment.post_id == post_id).all()


def create_comment(request: CommentBase, connection: Session, user: UserAuth):
    comment = DBComment(
        text=request.text,
        username=user.username,
        timestamp=datetime.datetime.now(),
        post_id=request.post_id
    )
    connection.add(comment)
    connection.commit()
    connection.refresh(comment)
    return comment
