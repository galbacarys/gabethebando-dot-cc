from pony.orm import ERDiagramError
from pony import orm

db = orm.Database()

def post_init():
    db.bind(provider="sqlite", filename="../db.sqlite3")
    db.generate_mapping(create_tables=True)
