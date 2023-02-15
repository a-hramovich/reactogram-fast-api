import random
import shutil
import string

from fastapi import APIRouter, UploadFile, File, Depends

from auth.oauth2 import get_current_user
from routers.schemas import UserAuth

router = APIRouter(
    prefix='/image',
    tags=['image'],
)


@router.post('')
def upload_file(request: UploadFile = File(...), current_user: UserAuth = Depends(get_current_user)):
    generated_name_prefix = ''.join(random.choice(string.ascii_letters) for i in range(6))
    new_name = f'{request.filename.split(".")[0]}_{generated_name_prefix}.{request.filename.split(".")[1]}'
    path = f'images/{new_name}'
    with open(path, 'w+b') as buffer:
        shutil.copyfileobj(request.file, buffer)
    return {'filename': path}
