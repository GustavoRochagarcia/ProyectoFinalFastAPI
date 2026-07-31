from sqlalchemy.orm import Session

from app.database.models import Post
from app.schemas.post import PostCreate, PostUpdate


def get_by_id(db: Session, post_id: int) -> Post | None:
    return db.get(Post, post_id)


def get_all(db: Session) -> list[Post]:
    return db.query(Post).order_by(Post.id).all()


def create(db: Session, data: PostCreate) -> Post:
    post = Post(**data.model_dump())
    db.add(post)
    db.commit()
    db.refresh(post)
    return post


def update(db: Session, post: Post, data: PostUpdate) -> Post:
    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(post, field, value)
    db.commit()
    db.refresh(post)
    return post


def delete(db: Session, post: Post) -> None:
    db.delete(post)
    db.commit()
