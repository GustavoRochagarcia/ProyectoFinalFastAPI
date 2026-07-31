from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.config import settings
from app.database.database import Base, engine
from app.database import models
from app.routes import posts, users


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(title=settings.APP_NAME, lifespan=lifespan)

app.include_router(users.router)
app.include_router(posts.router)
