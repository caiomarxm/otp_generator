import os
from typing import Literal
from pydantic import computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')

    NT_DB_FOLDER: str
    POSIX_DB_FOLDER: str

    @computed_field
    @property
    def db_url(self) -> str:
        home_dir = os.path.expanduser('~')
        # print(os.name)
        folder_dir = self.NT_DB_FOLDER if os.name == 'nt' else self.POSIX_DB_FOLDER
        return f"{home_dir}{folder_dir}pix_generator.db"

settings = Settings()
