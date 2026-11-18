from typing import Annotated, Literal

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

__all__ = ("settings", )


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    mode: Annotated[Literal["DEV", "PROD"], Field(..., alias="MODE")]
    docs_user: Annotated[str, Field(..., alias="DOCS_USER")]
    docs_password: Annotated[str, Field(..., alias="DOCS_PASSWORD")]


settings = Settings()
