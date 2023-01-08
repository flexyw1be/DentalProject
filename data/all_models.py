from peewee import *

db = SqliteDatabase('data/database.db')


class Doctor(Model):
    id = PrimaryKeyField(unique=True)
    last_name = AnyField(null=False)
    first_name = AnyField(null=False)
    middle_name = AnyField(null=True)
    current_name = AnyField(null=False)
    password = AnyField(null=False)
    address = AnyField(null=False)
    number = AnyField(null=False)
    date = AnyField(null=False)

    class Meta:
        database = db


class Admin(Model):
    id = PrimaryKeyField(unique=True)
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
    id = PrimaryKeyField(unique=True)
    last_name = AnyField(null=False)
    first_name = AnyField(null=False)
    middle_name = AnyField(null=True)
    current_name = AnyField(null=False)
    address = AnyField(null=False)
    number = AnyField(null=False)
    date = AnyField(null=False)

    class Meta:
        database = db


class Price(Model):
    id = PrimaryKeyField(unique=True)
    article = AnyField(null=False)
    price = IntegerField(null=False)

    class Meta:
        database = db


class Preparations(Model):
    id = PrimaryKeyField(unique=True)
    article = AnyField(null=False)
    name = AnyField(null=False)

    class Meta:
        database = db


class Services(Model):
    id = PrimaryKeyField(unique=True)
    article = AnyField(null=False)
    name = AnyField(null=False)

    class Meta:
        database = db


class Note(Model):
    id = PrimaryKeyField(unique=True)
    Patient_id = AnyField(null=False)
    Doctor_id = AnyField(null=False)
    date = DateTimeField(null=False)

    class Meta:
        database = db


Doctor.create_table()
LoginData.create_table()
Admin.create_table()
Patient.create_table()
Price.create_table()
Preparations.create_table()
Services.create_table()
Note.create_table()
