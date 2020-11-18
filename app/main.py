# -*- mode: python -*- -*- coding: utf-8 -*-
from fastapi import FastAPI

from .endpoints import router

app = FastAPI()

app.include_router(router)
