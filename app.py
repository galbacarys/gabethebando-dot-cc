from werkzeug.exceptions import NotFound
from pages import Pages
from threading import Thread
from time import sleep
from blog import Blog

from flask import Flask, render_template, send_from_directory
from werkzeug.middleware.proxy_fix import ProxyFix

blog = Blog()
pages = Pages()

app = Flask(__name__)
proxy_app = ProxyFix(app, x_for=1, x_host=1)


@app.context_processor
def inject_globals():
    return {"blog": blog, "pages": pages}


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


@app.route("/<path:path>")
def static_fallback(path):
    # Just return a file within static. send_from_directory handles
    # traversal attacks.
    return send_from_directory("./static/", path)
