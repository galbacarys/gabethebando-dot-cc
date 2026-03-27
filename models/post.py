from pony import orm

from . import db


class Post(db.Entity):
    slug = orm.Required(str)
    comments = orm.Set('Comment')

class Comment(db.Entity):
    post = orm.Required(Post)
    user = orm.Required(str)
    body = orm.Required(str)


