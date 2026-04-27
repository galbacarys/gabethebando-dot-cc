from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Length
from flask_wtf import FlaskForm
from pony.orm import desc, db_session, commit as orm_commit
from models.guestbook import GuestbookEntry
from flask import Blueprint, request, render_template, redirect, url_for
import os
import requests


guestbook_bp = Blueprint('guestbook_bp', __name__)


class GuestbookForm(FlaskForm):
    poster = StringField('poster', validators=[DataRequired(), Length(min=3, max=40)])
    post = TextAreaField('post', validators=[DataRequired(), Length(min=10, max=200)])

@guestbook_bp.route('/approve/<int:post_id>')
def approve_post(post_id):
    post = GuestbookEntry.get(id=post_id)
    proposed_nonce = request.args.get('q', default=None)
    if proposed_nonce:
        post.approve_post(proposed_nonce)


def email_post_approval_request(guestbook_post):
    endpoint = os.getenv('MAILGUN_ENDPOINT')
    api_key = os.getenv('MAILGUN_API_KEY')

    text = f"""
    New Guestbook Post to approve:

    Poster: {guestbook_post.poster}
    Post: {guestbook_post.post}

    To approve, click here: {
        "https://gabethebando.cc " + url_for('guestbook_bp.approve_post', post_id=guestbook_post.id, external=True) + "?q=" + guestbook_post.post_approval_nonce
    }
    """
    if os.getenv('TEST') is not None:
        print("Email sending disabled in test mode; automatically approving")
        with db_session:
            guestbook_post.post_approved = True
        return
    
    req = requests.post(
      	endpoint,
      	auth=("api", api_key),
      	data={"from": "Mailgun Sandbox <postmaster@sandboxa4fca2b749404604ba1808ee8534dd27.mailgun.org>",
    		"to": "Gabe The Bando <gabethebando@proton.me>",
      		"subject": "New guestbook post to approve",
             "text": text
             }
        )
    if not req.ok:
        # delete the post and raise an exception
        with db_session:
            guestbook_post.delete()
        raise Exception("Could not reach mailgun!")


@guestbook_bp.route('/', methods=['GET','POST'])
@db_session
def index():
    form = GuestbookForm()
    if form.validate_on_submit():
        poster = form.poster.data
        post = form.post.data
        new_guestbook_post = GuestbookEntry(poster=poster, post=post)
        orm_commit()
        email_post_approval_request(new_guestbook_post)
        return redirect(url_for('guestbook_bp.index'))
    form_errors = form.errors
    page = int(request.args.get('page', default=1))
    posts = GuestbookEntry.select(post_approved=True).order_by(desc(GuestbookEntry.post_time)).page(page, pagesize=10)

    total_posts = GuestbookEntry.select().count()
    has_more_pages = (page * 10) < total_posts
    print(f"{page} {has_more_pages} {total_posts}")

    return render_template('guestbook.html', 
                           form=form, 
                           form_errors=form_errors,
                           page=page, 
                           has_more_pages=has_more_pages, 
                           posts=posts)
