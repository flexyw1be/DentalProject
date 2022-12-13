def get_without_failing(Model, query):
    results = Model.select().where(query)
    return results if len(results) > 0 else None
