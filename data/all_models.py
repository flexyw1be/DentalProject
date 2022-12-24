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


class LoginData(Model):
    id = PrimaryKeyField(unique=True)
    login = AnyField(null=False)
    password = CharField(null=False)

    class Meta:
        database = db


class Patient(Model):
    last_name = AnyField(null=False)
    first_name = AnyField(null=False)
    middle_name = AnyField(null=True)
    current_name = AnyField(null=False)
    address = AnyField(null=False)
    number = AnyField(null=False)
    date = AnyField(null=False)

    class Meta:
        database = db


Doctor.create_table()
LoginData.create_table()
Admin.create_table()
Patient.create_table()
