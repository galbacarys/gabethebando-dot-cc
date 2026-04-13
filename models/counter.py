from pony.orm import db_session
from datetime import datetime
from . import db, orm


class Counter(db.Entity):
    page_url = orm.PrimaryKey(str, auto=False)
    updated = orm.Required(datetime, default=datetime.now)
    count = orm.Required(int)


@orm.db_session
def inc_counter(page_url):
    c = Counter.get(page_url=page_url)
    if not c:
        c = Counter(page_url=page_url, count=1)
    c.count += 1


@orm.db_session
def get_counter(page_url):
    c = Counter.get(page_url=page_url)
    if not c:
        c = Counter(page_url=page_url, count=1)
    return c.count
