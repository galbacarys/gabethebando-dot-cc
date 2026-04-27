from pony.orm import db_session
from datetime import datetime
from secrets import token_hex

from . import db, orm


def generate_nonce():
    """Generate an approval nonce (a crypto-safe 64 character string)"""
    return token_hex(32)


class GuestbookEntry(db.Entity):
    poster = orm.Required(str)
    post = orm.Required(str, max_len=200) # like a tweet ish
    post_time = orm.Required(datetime, default=datetime.now)
    post_approved = orm.Required(bool, default=False)
    post_approval_nonce = orm.Required(str, default=generate_nonce)
    

    @orm.db_session
    def approve_post(self, proposed_nonce):
        if self.post_approval_nonce == proposed_nonce:
            self.post_approved = True
        else:
            print(f"WARNING: Invalid nonce provided for post: {self.id}")
