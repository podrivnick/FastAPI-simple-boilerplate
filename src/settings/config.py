from pydantic import Field
from pydantic_settings import BaseSettings


class Config(BaseSettings):
    postgres_db: str = Field(alias="POSTGRES_DB")
    postgres_user: str = Field(alias="POSTGRES_USER")
    postgres_password: str = Field(alias="POSTGRES_PASSWORD")
    postgres_host: str = Field(alias="POSTGRES_HOST")
    postgres_port: str = Field(alias="POSTGRES_PORT")

    debug: bool = Field(default=True, alias="DEBUG")

    api_host: str = Field(alias="API_HOST")
    api_port: str = Field(alias="API_PORT")
