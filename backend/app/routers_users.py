from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import get_db
from . import schemas, crud

router = APIRouter(
    prefix="/user",
    tags=["Users"]
)


# --------------------------
# Create a New User
# --------------------------

@router.post("/create", response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    """
    Creates a new TradeLens user with email, risk tolerance,
    and investment horizon.
    """
    
    # If email was provided, check for duplicates
    if user.email:
        existing = db.query(crud.models.User).filter(crud.models.User.email == user.email).first()
        if existing:
            raise HTTPException(status_code=400, detail="Email already exists")

    new_user = crud.create_user(db, user)
    return new_user
