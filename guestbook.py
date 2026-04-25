import logging
from logging import log
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Length
from flask_wtf import FlaskForm
from pony.orm import desc, db_session
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
        url_for('guestbook_bp.approve_post', id=guestbook_post.id, external=True) + "?q=" + guestbook_post.approval_nonce
    }
    """
    logging.info('Sending message for approval')
    
    return requests.post(
      	endpoint,
      	auth=("api", api_key),
      	data={"from": "Mailgun Sandbox <postmaster@sandboxa4fca2b749404604ba1808ee8534dd27.mailgun.org>",
    		"to": "Gabe Albacarys <gabethebando@proton.me>",
      		"subject": "New guestbook post to approve",
             "text": text
             }
        )


@guestbook_bp.route('/', methods=['GET','POST'])
@db_session
def index():
    form = GuestbookForm()
    if form.validate_on_submit():
        print("asdf")
        poster = form.poster.data
        post = form.post.data
        new_guestbook_post = GuestbookEntry(poster=poster, post=post)
        email_post_approval_request(new_guestbook_post)
        return redirect(url_for('guestbook_bp.index'))
    page = request.args.get('page', default=1)
    posts = GuestbookEntry.select().order_by(desc(GuestbookEntry.post_time)).page(page, pagesize=25)

    total_posts = GuestbookEntry.select().count()
    remaining_pages = (page * 25) < total_posts

    return render_template('guestbook.html', 
                           form=form, 
                           page=page, 
                           remaining_pages=remaining_pages, 
                           posts=posts)
