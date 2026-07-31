from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.database.models import Comment
from app.repositories import comment_repository, post_repository, user_repository
from app.schemas.comment import CommentCreate, CommentUpdate


def _ensure_user_exists(db: Session, user_id: int) -> None:
    if not user_repository.get_by_id(db, user_id):
        raise HTTPException(status.HTTP_404_NOT_FOUND, "User not found")


def _ensure_post_exists(db: Session, post_id: int) -> None:
    if not post_repository.get_by_id(db, post_id):
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Post not found")


def create_comment(db: Session, data: CommentCreate) -> Comment:
    _ensure_user_exists(db, data.user_id)
    _ensure_post_exists(db, data.post_id)
    return comment_repository.create(db, data)


def list_comments(db: Session) -> list[Comment]:
    return comment_repository.get_all(db)


def get_comment(db: Session, comment_id: int) -> Comment:
    comment = comment_repository.get_by_id(db, comment_id)
    if not comment:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Comment not found")
    return comment


def update_comment(db: Session, comment_id: int, data: CommentUpdate) -> Comment:
    comment = get_comment(db, comment_id)
    if data.user_id and not user_repository.get_by_id(db, data.user_id):
        raise HTTPException(status.HTTP_404_NOT_FOUND, "User not found")
    if data.post_id and not post_repository.get_by_id(db, data.post_id):
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Post not found")
    return comment_repository.update(db, comment, data)


def delete_comment(db: Session, comment_id: int) -> None:
    comment = get_comment(db, comment_id)
    comment_repository.delete(db, comment)
