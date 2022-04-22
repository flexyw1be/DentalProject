import datetime

from peewee import *

db = SqliteDatabase('members.db')


class Member(Model):
    __tablename__ = 'users'

    id = PrimaryKeyField(unique=True)
    name = CharField(null=False)
    lvl = FloatField(null=False)
    role = CharField(null=False)
    created_date = DateField(default=datetime.datetime.now)

    class Meta:
        database = db
        order_by = 'lvl'