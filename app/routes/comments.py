from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.comment import CommentCreate, CommentOut, CommentUpdate
from app.services import comment_service

router = APIRouter(prefix="/comments", tags=["comments"])


@router.post("", response_model=CommentOut, status_code=status.HTTP_201_CREATED)
def create_comment(data: CommentCreate, db: Session = Depends(get_db)) -> CommentOut:
    return comment_service.create_comment(db, data)


@router.get("", response_model=list[CommentOut])
def list_comments(db: Session = Depends(get_db)) -> list[CommentOut]:
    return comment_service.list_comments(db)


@router.get("/{comment_id}", response_model=CommentOut)
def get_comment(comment_id: int, db: Session = Depends(get_db)) -> CommentOut:
    return comment_service.get_comment(db, comment_id)


@router.put("/{comment_id}", response_model=CommentOut)
def update_comment(comment_id: int, data: CommentUpdate, db: Session = Depends(get_db)) -> CommentOut:
    return comment_service.update_comment(db, comment_id, data)


@router.delete("/{comment_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_comment(comment_id: int, db: Session = Depends(get_db)) -> None:
    comment_service.delete_comment(db, comment_id)
