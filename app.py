from threading import Thread
from utils.onlyone import only_one
from time import sleep
from blog import Blog

from flask import Flask, render_template
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)
proxy_app = ProxyFix(app, x_for=1, x_host=1)

blog = Blog()


@app.route("/")
def homepage():
    return render_template("index.html", posts=blog.get_posts())


@app.route("/post/<string:slug>")
def post(slug):
    post = blog.get_post(slug)
    return render_template("post.html", post=post)
