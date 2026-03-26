from markdown import markdown
import frontmatter
import casefy
from dateutil.parser import parse as parse_date, ParserError


from datetime import datetime
from dataclasses import dataclass
from pathlib import Path
import sys


class Blog:
    def __init__(self):
        self.posts = {}
        posts_path = Path("posts/")
        for file_path in posts_path.iterdir():
            with open(file_path, "r") as f:
                print(f"Processing file {file_path}")
                post = frontmatter.load(f)
                metadata = post.metadata
                if not is_metadata_valid(metadata):
                    continue
                title = str(metadata["title"])
                date = parse_date(metadata["date"])
                content = post.content
                html_content = markdown(content, extensions=["fenced_code", "tables"])
                new_post = BlogPost(
                    title=title, date=date, content=content, html_content=html_content
                )
                self.posts[new_post.slug()] = new_post
                print(f"Processed post '{title}'")

    def get_post(self, slug):
        if slug in self.posts:
            return self.posts[slug]
        return None

    def get_posts(self, lim=10):
        posts = [post for _, post in self.posts.items()]
        return sorted(posts, key=lambda post: post.date, reverse=True)[:lim]


@dataclass
class BlogPost:
    title: str
    date: datetime
    content: str
    html_content: str

    def slug(self):
        return make_slug(self.title)


def is_metadata_valid(metadata):
    required_keys = ["title", "date"]
    for key in required_keys:
        if key not in metadata.keys():
            print(f"Key {key} missing in {metadata}")
            return False
    # make sure the date is parseable
    try:
        parse_date(metadata["date"])
    except ParserError:
        print(f"Unable to parse date {metadata['date']}", file=sys.stderr)
    return True


def make_slug(title):
    return casefy.kebabcase(title)
