from fastapi import APIRouter, Depends, HTTPException
from google.cloud.firestore import Client
from .database import get_db
from . import crud, schemas

router = APIRouter(prefix="/user", tags=["Users"])

@router.post("/create", response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Client = Depends(get_db)):
    # Check duplicate email
    if user.email:
        existing = crud.get_user_by_email(db, user.email)
        if existing:
            raise HTTPException(status_code=400, detail="Email already exists")

    new_user = crud.create_user(db, user)
    return new_user
