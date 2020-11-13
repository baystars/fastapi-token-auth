# -*- mode: python -*- -*- coding: utf-8 -*-
from functools import lru_cache
import os
from pathlib import Path
from typing import Optional

from pydantic import BaseSettings

APP_DIR = os.path.abspath(os.path.dirname(__file__))
PROJECT_DIR = Path(APP_DIR).parent
DATA_DIR = os.path.join(PROJECT_DIR, 'data')

class Settings(BaseSettings):
    debug: bool = False
    secret_key: Optional[bytes] = os.urandom(24)
    backend_cors_origins: Optional[str] = '*'
    db_path = os.path.join(DATA_DIR, 'data.db')
    test_user: Optional[str] = 'john'
    test_password: Optional[str] = 'doe'

    class Config:
        env_file = os.path.join(PROJECT_DIR, '.env')
        env_file_encoding = 'utf-8'
        case_sensitive = True

@lru_cache()
def get_settings():
    return Settings()
settings = get_settings()
