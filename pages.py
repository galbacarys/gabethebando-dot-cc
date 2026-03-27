from markdown import markdown
import frontmatter
import casefy
from dateutil.parser import parse as parse_date, ParserError


from datetime import datetime
from dataclasses import dataclass
from pathlib import Path
import sys

class Pages:
    def __init__(self):
        self.pages = {}
        pages_path = Path("pages/")
        for file_path in pages_path.iterdir():
            with open(file_path, "r") as f:
                print(f"Processing file {file_path}")
                post = frontmatter.load(f)
                metadata = post.metadata
                if not is_metadata_valid(metadata):
                    continue
                title = str(metadata["title"])
                content = post.content
                html_content = markdown(content, extensions=["fenced_code", "tables"])
                new_page = Page(
                    title=title, content=content, html_content=html_content
                )
                self.pages[new_page.slug()] = new_page
                print(f"Processed post '{title}'")

    def get_page(self, slug):
        if slug in self.pages:
            return self.pages[slug]
        return None

    def get_pages(self):
        return [page for _, page in self.pages.items()]


@dataclass
class Page:
    title: str
    content: str
    html_content: str

    def slug(self):
        return make_slug(self.title)


def is_metadata_valid(metadata):
    required_keys = ["title"]
    for key in required_keys:
        if key not in metadata.keys():
            print(f"Key {key} missing in {metadata}")
            return False
    return True


def make_slug(title):
    return casefy.kebabcase(title)
