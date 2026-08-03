import os
from guestbook import guestbook_bp
from werkzeug.exceptions import NotFound
from pages import Pages
from blog import Blog
from models import counter, post_init

from flask import Flask, render_template, send_from_directory, request, redirect
from werkzeug.middleware.proxy_fix import ProxyFix

from time import sleep
from threading import Thread

blog = Blog()
pages = Pages()

app = Flask(__name__)
proxy_app = ProxyFix(app, x_for=1, x_host=1)

# CSRF configuration
with open('/tmp/ephemeral-app-secret', 'r') as f:
    app.config['SECRET_KEY'] = f.read()

app.register_blueprint(guestbook_bp, url_prefix='/guestbook')

# Initialize all the models
post_init()


@app.context_processor
def inject_globals():
    return {
        "blog": blog,
        "pages": pages,
        "view_count": counter.get_counter(request.path),
    }


@app.before_request
def counters():
    url = request.path
    counter.inc_counter(url)


@app.route("/")
def homepage():
    return render_template("index.html")


@app.route("/post/<string:slug>")
def post(slug):
    post = blog.get_post(slug)
    if not post:
        raise NotFound()
    return render_template("post.html", post=post)


@app.route("/post/archive")
def archive():
    return render_template("archive.html")


@app.route("/page/<string:slug>")
def page(slug):
    page = pages.get_page(slug)
    if not page:
        raise NotFound()
    return render_template("page.html", page=page)

@app.route("/resume")
def resume():
    return redirect('https://gabethebando-assets.nyc3.cdn.digitaloceanspaces.com/Resume-26.pdf')


@app.route("/<path:path>")
def static_fallback(path):
    # Just return a file within static. send_from_directory handles
    # traversal attacks.
    return send_from_directory("./static/", path)
