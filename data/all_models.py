import datetime

from peewee import *

db = SqliteDatabase('data/database.db')


class LoginData(Model):
    __tablename__ = 'users'

    id = PrimaryKeyField(unique=True)
    login = CharField(null=False)
    password = CharField(null=False)

    class Meta:
        database = db


LoginData.create_table()