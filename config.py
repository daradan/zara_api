import os
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())


class Settings:
    TOKEN: str = os.getenv("TOKEN")


settings = Settings()
