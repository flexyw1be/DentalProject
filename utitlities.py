import sys


def get_without_failing(model, query):
    results = model.select().where(query)
    return results if len(results) > 0 else None


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)
