from peewee import *

db = SqliteDatabase('data/database.db')


class Doctor(Model):
    id = AutoField(unique=True)
    last_name = AnyField(null=False)
    first_name = AnyField(null=False)
    middle_name = AnyField(null=True)
    current_name = AnyField(null=False)
    password = AnyField(null=False)
    address = AnyField(null=True)
    number = AnyField(null=True)
    date = AnyField(null=True)

    class Meta:
        database = db


class Admin(Model):
    id = AutoField(unique=True)
    last_name = AnyField(null=False)
    first_name = AnyField(null=False)
    middle_name = AnyField(null=True)
    current_name = AnyField(null=False)
    password = AnyField(null=False)

    class Meta:
        database = db


class Patient(Model):
    id = AutoField(unique=True)
    last_name = AnyField(null=False)
    first_name = AnyField(null=False)
    middle_name = AnyField(null=True)
    current_name = AnyField(null=False)
    address = AnyField(null=True)
    number = AnyField(null=True)
    date = AnyField(null=True)

    class Meta:
        database = db


class Price(Model):
    id = AutoField(unique=True)
    article = IntegerField(null=False)
    price = IntegerField(null=False)

    class Meta:
        database = db


class Preparations(Model):
    id = AutoField(unique=True)
    article = AnyField(null=False)
    name = AnyField(null=False)

    class Meta:
        database = db


class Services(Model):
    id = AutoField(unique=True)
    article = AnyField(null=False)
    name = AnyField(null=False)

    class Meta:
        database = db


class Note(Model):
    id = AutoField(unique=True)
    Patient_id = AnyField(null=False)
    Doctor_id = AnyField(null=False)
    date = AnyField(null=True)
    start_time = TimeField(null=True)
    finish_time = TimeField(null=True)
    status = AnyField(null=True)

    class Meta:
        database = db


class History(Model):
    id = AutoField(unique=True)
    name = AnyField(null=False)
    datetime = AnyField(null=True)
    Patient_id = AnyField(null=False)
    Doctor_id = AnyField(null=False)
    list_of_services = AnyField(null=False)
    amount = AnyField(null=False)
    note = AnyField(null=False)
    class Meta:
        database = db



Doctor.create_table()
# LoginData.create_table()
Admin.create_table()
Patient.create_table()
Price.create_table()
Preparations.create_table()
Services.create_table()
Note.create_table()
History.create_table()
