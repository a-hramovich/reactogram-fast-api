from sqlalchemy.orm import Session

from db.hashing import Hash
from db.models import DBUser
from routers.schemas import UserBase


def create_user(request: UserBase, connection: Session):
    model = DBUser(
        username=request.username,
        email=request.email,
        password=Hash().bcrypt(request.password)
    )
    connection.add(model)
    connection.commit()
    connection.refresh(model)
    return model


def get_user_by_username(connection: Session, username):
    return connection.query(DBUser).filter(DBUser.username == username).first()
