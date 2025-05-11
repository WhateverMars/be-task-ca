from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..common import get_db
from .repository import UserRepository
from .services import UserService

from .schema import CreateUserRequest


user_router = APIRouter(
    prefix="/users",
    tags=["user"],
)


@user_router.post("/")
async def create_user(user: CreateUserRequest, db: Session = Depends(get_db)):
    user_repository = UserRepository(db)
    user_service = UserService(user_repository)
    try:
        return user_service.create_user(user)
    except Exception as e:
        raise HTTPException(
            status_code=409, detail=str(e)
        )
