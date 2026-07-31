from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.post import PostCreate, PostOut, PostUpdate
from app.services import post_service

router = APIRouter(prefix="/posts", tags=["posts"])


@router.post("", response_model=PostOut, status_code=status.HTTP_201_CREATED)
def create_post(data: PostCreate, db: Session = Depends(get_db)) -> PostOut:
    return post_service.create_post(db, data)


@router.get("", response_model=list[PostOut])
def list_posts(db: Session = Depends(get_db)) -> list[PostOut]:
    return post_service.list_posts(db)


@router.get("/{post_id}", response_model=PostOut)
def get_post(post_id: int, db: Session = Depends(get_db)) -> PostOut:
    return post_service.get_post(db, post_id)


@router.put("/{post_id}", response_model=PostOut)
def update_post(post_id: int, data: PostUpdate, db: Session = Depends(get_db)) -> PostOut:
    return post_service.update_post(db, post_id, data)


@router.delete("/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(post_id: int, db: Session = Depends(get_db)) -> None:
    post_service.delete_post(db, post_id)
