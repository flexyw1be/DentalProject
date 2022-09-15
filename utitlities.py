def get_without_failing(Model, query):
    results = Model.select().where(query).limit(1)
    return results[0] if len(results) > 0 else None
