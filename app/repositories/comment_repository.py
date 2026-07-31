from sqlalchemy.orm import Session

from app.database.models import Comment
from app.schemas.comment import CommentCreate, CommentUpdate


def get_by_id(db: Session, comment_id: int) -> Comment | None:
    return db.get(Comment, comment_id)


def get_all(db: Session) -> list[Comment]:
    return db.query(Comment).order_by(Comment.id).all()


def create(db: Session, data: CommentCreate) -> Comment:
    comment = Comment(**data.model_dump())
    db.add(comment)
    db.commit()
    db.refresh(comment)
    return comment


def update(db: Session, comment: Comment, data: CommentUpdate) -> Comment:
    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(comment, field, value)
    db.commit()
    db.refresh(comment)
    return comment


def delete(db: Session, comment: Comment) -> None:
    db.delete(comment)
    db.commit()
