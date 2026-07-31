from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class CommentBase(BaseModel):
    content: str = Field(min_length=1)
    user_id: int
    post_id: int


class CommentCreate(CommentBase):
    pass


class CommentUpdate(BaseModel):
    content: str | None = Field(default=None, min_length=1)
    user_id: int | None = None
    post_id: int | None = None


class CommentOut(CommentBase):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
