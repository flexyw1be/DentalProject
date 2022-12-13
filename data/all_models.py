from peewee import *

db = SqliteDatabase('data/database.db')


class LoginData(Model):
    id = PrimaryKeyField(unique=True)
    login = AnyField(null=False)
    password = CharField(null=False)

    class Meta:
        database = db


class Doctor(Model):
    first_name = AnyField(null=False)
    last_name = AnyField(null=False)
    middle_name = AnyField(null=True)
    login = AnyField(null=False)

    class Meta:
        database = db


class Admin(Model):
    first_name = AnyField(null=False)
    last_name = AnyField(null=False)
    middle_name = AnyField(null=True)
    login = AnyField(null=False)

    class Meta:
        database = db


LoginData.create_table()
Doctor.create_table()
Admin.create_table()
