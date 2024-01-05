import os
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import AnyHttpUrl
from enum import Enum


class ModeEnum(str, Enum):
    development = "development"
    production = "production"
    testing = "testing"    


class Settings(BaseSettings):
    MODE: ModeEnum = ModeEnum.development
    API_VERSION: str = "v1"
    API_V1_STR: str = f"/api/{API_VERSION}"
    WEATHER_URL: AnyHttpUrl

    model_config = SettingsConfigDict(
        case_sensitive=True, env_file=os.path.expanduser("~/.env")
    )


settings = Settings()