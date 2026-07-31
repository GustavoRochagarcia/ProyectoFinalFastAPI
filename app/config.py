import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    APP_NAME: str = os.getenv("APP_NAME", "ProyectoFinalFastAPI")
    DEBUG: bool = os.getenv("DEBUG", "False").lower() in ("1", "true", "yes", "on")
    SECRET_KEY: str = os.getenv("SECRET_KEY", "")
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./app.db")

    def __init__(self) -> None:
        if not self.SECRET_KEY:
            raise ValueError("SECRET_KEY must be set via environment or .env file")


settings = Settings()
