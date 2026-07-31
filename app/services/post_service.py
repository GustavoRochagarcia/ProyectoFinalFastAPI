from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.database.models import Post
from app.repositories import post_repository, user_repository
from app.schemas.post import PostCreate, PostUpdate


def _ensure_user_exists(db: Session, user_id: int) -> None:
    if not user_repository.get_by_id(db, user_id):
        raise HTTPException(status.HTTP_404_NOT_FOUND, "User not found")


def create_post(db: Session, data: PostCreate) -> Post:
    _ensure_user_exists(db, data.user_id)
    return post_repository.create(db, data)


def list_posts(db: Session) -> list[Post]:
    return post_repository.get_all(db)


def get_post(db: Session, post_id: int) -> Post:
    post = post_repository.get_by_id(db, post_id)
    if not post:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Post not found")
    return post


def update_post(db: Session, post_id: int, data: PostUpdate) -> Post:
    post = get_post(db, post_id)
    if data.user_id and not user_repository.get_by_id(db, data.user_id):
        raise HTTPException(status.HTTP_404_NOT_FOUND, "User not found")
    return post_repository.update(db, post, data)


def delete_post(db: Session, post_id: int) -> None:
    post = get_post(db, post_id)
    post_repository.delete(db, post)
