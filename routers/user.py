from fastapi import APIRouter, Depends

from db.db import get_db
from db.db_user import create_user
from routers.schemas import UserDisplay, UserBase

router = APIRouter(
    prefix='/user',
    tags=['user'],
)


@router.post('', response_model=UserDisplay)
def create_new_user(request: UserBase, db=Depends(get_db)):
    return create_user(request, db)
