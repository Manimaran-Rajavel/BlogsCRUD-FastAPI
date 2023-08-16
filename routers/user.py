from fastapi import APIRouter, Depends, status, HTTPException
import schemas as s, models as md
from sqlalchemy.orm import session
from database import get_db

router = APIRouter(
    prefix='/user',
    tags=['User']
)

@router.post('', status_code=status.HTTP_201_CREATED)
def create_user(request: s.User, db: session = Depends(get_db)):
    new_user = md.User_Model(name= request.name, email= request.email, password= request.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get('/{id}',status_code=status.HTTP_200_OK ,response_model=s.ShowUser)
def show_user(id: int, db: session = Depends(get_db)):
    user = db.query(md.User_Model).filter(md.User_Model.id == id).first()
    if not user:
        HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Detail {id} was not Found")
    return user