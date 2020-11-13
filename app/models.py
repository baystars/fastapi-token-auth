# -*- mode: python -*- -*- coding: utf-8 -*-
from peewee import (SqliteDatabase, Model, AutoField, CharField, TextField)

from app.config import settings

db = SqliteDatabase(settings.db_path)

class User(Model):
    id = AutoField(primary_key=True)
    name = CharField(100)
    password = CharField(100)
    refresh_token = TextField(null=True)

    class Meta:
        database = db

db.create_tables([User])

User.create(name=settings.test_user, password=settings.test_password)
