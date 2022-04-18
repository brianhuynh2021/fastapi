from .. import models, schemas, utils
from sqlalchemy.orm import Session
from ..database import get_db
from fastapi import APIRouter, Response, status, HTTPException, Depends
from typing import Optional, List

router = APIRouter(
    prefix="/users",
    tags=['Users']
)

@router.post("/createuser", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def create_user(user: schemas.User, db: Session = Depends(get_db)):
    # Hash the password - user.password
    hased_password = utils.hashed_password(user.password)
    user.password = hased_password
    
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get("", response_model=List[schemas.User])
def get_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users

@router.get("/{id}", response_model=schemas.UserOut)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        # response.status_code = 404
        # return {'message': f'post with id {id} was not found'}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} was not found")
    return user