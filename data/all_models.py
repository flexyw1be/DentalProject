import datetime

from peewee import *

db = SqliteDatabase('data/database.db')


class LoginData(Model):

    id = PrimaryKeyField(unique=True)
    login = AnyField(null=False)
    password = CharField(null=False)

    class Meta:
        database = db


LoginData.create_table()