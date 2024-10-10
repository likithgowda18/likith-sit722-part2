import os

class Settings:
    DATABASE_URL: str = os.getenv("postgresql://bookdb_9v1l_user:vV8FHZWV8peiImLkZzYRFxE782jkDoI1@dpg-cs3mhlggph6c73c4dltg-a.oregon-postgres.render.com/bookdb_9v1l")

settings = Settings()
