import os
from urllib.parse import urlparse

import yaml
import markdown


class Globals:
    def __init__(self, base_url, src_dir):
        self.base_url = base_url
        self.src_dir = src_dir

    def static(self, path):
        path = os.path.join("assets", path)
        return "/" + path.removeprefix("/")

    def load_header_context(self):
        with open(os.path.join(self.src_dir, "header_context.yml")) as f:
            return yaml.safe_load(f)

    def get_nav_link(self, item):
        if "index" in item:
            link = item["index"].removesuffix("index")
            if link != "":
                link = link.removesuffix("/")
        else:
            link = item["link"]

        return "/" + link.removeprefix("/")

    def static_or_abs_link(self, item):
        parsed = urlparse(item)
        if not parsed.netloc:
            return self.static(parsed.path)
        return item

    def sum_attr(self, list_, attr):
        return sum(int(x[attr]) for x in list_)

    def markdown(self, content):
        return markdown.markdown(content, extensions=["nl2br", "mdx_math"])

    def get(self):
        return {
            "static": self.static,
            "header_context": self.load_header_context(),
            "get_nav_link": self.get_nav_link,
            "sum_attr": self.sum_attr,
            "markdown": self.markdown,
            "static_or_abs_link": self.static_or_abs_link,
        }
