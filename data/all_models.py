from peewee import *

db = SqliteDatabase('data/database.db')


class Doctor(Model):
    last_name = AnyField(null=False)
    first_name = AnyField(null=False)
    middle_name = AnyField(null=True)
    current_name = AnyField(null=False)
    password = AnyField(null=False)

    class Meta:
        database = db


class Admin(Model):
    last_name = AnyField(null=False)
    first_name = AnyField(null=False)
    middle_name = AnyField(null=True)
    current_name = AnyField(null=False)
    password = AnyField(null=False)

    class Meta:
        database = db


Doctor.create_table()
Admin.create_table()
