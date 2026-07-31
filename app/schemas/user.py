from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class UserBase(BaseModel):
    given_name: str = Field(min_length=1, max_length=255)
    family_name: str = Field(min_length=1, max_length=255)
    email: EmailStr
    phone_number: str = Field(min_length=1, max_length=50)


class UserCreate(UserBase):
    pass


class UserUpdate(BaseModel):
    given_name: str | None = Field(default=None, min_length=1, max_length=255)
    family_name: str | None = Field(default=None, min_length=1, max_length=255)
    email: EmailStr | None = None
    phone_number: str | None = Field(default=None, min_length=1, max_length=50)


class UserOut(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
