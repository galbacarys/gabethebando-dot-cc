from pony import orm

db = orm.Database()

db.bind(provider="sqlite", filename="db.sqlite3")

db.generate_mapping(create_tables=True)
