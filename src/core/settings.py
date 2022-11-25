from pydantic import BaseSettings, Field
from dotenv import load_dotenv, dotenv_values


class Settings(BaseSettings):
    APP_ENV: str
    DATABASE_USERNAME: str
    DATABASE_PASSWORD: str
    DATABASE_HOST: str
    DATABASE_NAME: str
    DATABASE_PORT: str

    TEST_DATABASE_NAME: str

    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    class Config:
        env_file = ".env"


conf = dict(dotenv_values(".env"))
settings = Settings(**conf)

