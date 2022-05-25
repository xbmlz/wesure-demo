from pydantic import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "FastAPI"
    PROJECT_VERSION: str = "0.0.1"
    API_V1_STR: str = "/api/v1"

    class config:
        case_sensitive = True


settings = Settings()
