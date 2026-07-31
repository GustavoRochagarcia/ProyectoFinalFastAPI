from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.database.models import User
from app.repositories import user_repository
from app.schemas.user import UserCreate, UserUpdate


def create_user(db: Session, data: UserCreate) -> User:
    if user_repository.get_by_email(db, data.email):
        raise HTTPException(status.HTTP_400_BAD_REQUEST, "Email already registered")
    return user_repository.create(db, data)


def list_users(db: Session) -> list[User]:
    return user_repository.get_all(db)


def search_users(db: Session, given_name: str) -> list[User]:
    return user_repository.get_by_given_name(db, given_name)


def get_user(db: Session, user_id: int) -> User:
    user = user_repository.get_by_id(db, user_id)
    if not user:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "User not found")
    return user


def update_user(db: Session, user_id: int, data: UserUpdate) -> User:
    user = get_user(db, user_id)
    if data.email and user_repository.get_by_email(db, data.email):
        raise HTTPException(status.HTTP_400_BAD_REQUEST, "Email already registered")
    return user_repository.update(db, user, data)


def delete_user(db: Session, user_id: int) -> None:
    user = get_user(db, user_id)
    user_repository.delete(db, user)
