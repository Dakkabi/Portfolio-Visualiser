from dotenv import load_dotenv
from pydantic import computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict
import psycopg2

load_dotenv() # Load .env into memory

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
        extra="ignore",
        env_ignore_empty=True
    )

    POSTGRESQL_USERNAME: str
    POSTGRESQL_PASSWORD: str
    POSTGRESQL_SERVER: str
    POSTGRESQL_PORT: int
    POSTGRESQL_DATABASE: str
    POSTGRESQL_TEST_DATABASE: str

    JWT_SECRET_KEY: str
    AES_SECRET_KEY: str

    @computed_field
    @property
    def SQLALCHEMY_DATABASE_URI(self) -> str:
        return "{}://{}:{}@{}:{}/{}".format(
            "postgresql+psycopg2",
            self.POSTGRESQL_USERNAME,
            self.POSTGRESQL_PASSWORD,
            self.POSTGRESQL_SERVER,
            self.POSTGRESQL_PORT,
            self.POSTGRESQL_DATABASE
        )
