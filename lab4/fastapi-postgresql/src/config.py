from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    database_url: str
    alembic_url: str = ""

    def model_post_init(self, __context):
        self.alembic_url = self.database_url.replace("asyncpg", "psycopg2")

    class Config:
        env_file = ".env"
        env_prefix = ""

settings = Settings()
print(settings.alembic_url)