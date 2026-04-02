from datetime import datetime
from . import db, orm


class GrafittiPost(db.Entity):
    posted = orm.Required(datetime, default=datetime.now)
    poster = orm.Required(str)
    body = orm.Required(str, 400)
