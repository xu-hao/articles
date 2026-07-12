#!/usr/bin/env python3
"""Render an article for GitHub Pages and hand off to the Medium import tool.

Usage:
    ./publish.py <article>.md [--desc "index blurb"] [--no-push]

Renders <article>.md to <article>.html with the shared page template,
adds an index.html entry if missing, commits, pushes, waits for the
Pages build, and prints the canonical URL to paste into
https://medium.com/p/import.
"""

import argparse
import datetime
import html
import json
import re
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

REPO_DIR = Path(__file__).resolve().parent
SITE_URL = "https://xu-hao.github.io/articles"
PAGES_API = "repos/xu-hao/articles/pages/builds/latest"

STYLE = (
    "body{max-width:42em;margin:2em auto;font-family:Georgia,serif;line-height:1.6}"
    "pre{background:#f4f4f4;padding:1em;overflow-x:auto;font-size:14px}"
    "code{font-family:monospace}"
    "blockquote{border-left:3px solid #ccc;margin-left:0;padding-left:1em;color:#444}"
)


def esc_title(text):
    return (
        text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        .replace("'", "&#39;").replace('"', "&quot;")
    )


def postprocess(body):
    # Committed HTML keeps literal double quotes in prose; only <pre> blocks
    # retain &quot; from the renderer. Inside <pre>, newlines become <br> —
    # rendered identically by browsers, but Medium's import tool collapses
    # literal newlines and preserves <br>.
    parts = re.split(r"(<pre>.*?</pre>)", body, flags=re.S)
    out = []
    for p in parts:
        if p.startswith("<pre>"):
            out.append(p.replace("\n</code>", "</code>").replace("\n", "<br>"))
        else:
            out.append(p.replace("&quot;", '"'))
    return "".join(out)


def render(md_path):
    body = subprocess.run(
        ["markdown-it", str(md_path)], check=True, capture_output=True, text=True
    ).stdout.rstrip("\n")
    body = postprocess(body)
    m = re.search(r"<h1>(.*?)</h1>", body, flags=re.S)
    if not m:
        sys.exit("error: article needs a leading '# Title' heading")
    title = re.sub(r"<[^>]+>", "", m.group(1))
    page = (
        f'<html><head><meta charset="utf-8"><title>{esc_title(title)}</title>'
        f"<style>{STYLE}</style></head><body>{body}</body></html>"
    )
    return title, page


def ensure_index_entry(slug, title, desc):
    index = REPO_DIR / "index.html"
    text = index.read_text()
    if f'"{slug}.html"' in text:
        return False
    today = datetime.date.today().isoformat()
    entry = (
        f'<li><a href="{slug}.html">{esc_title(title)}</a> '
        f"<small>&mdash; {today} &middot; {desc}</small></li>"
    )
    text = text.replace("<ul>", f"<ul>\n{entry}", 1)
    index.write_text(text)
    return True


def git(*args, **kwargs):
    return subprocess.run(["git", "-C", str(REPO_DIR), *args], check=True, **kwargs)


def wait_for_pages(slug, title, timeout=300):
    deadline = time.time() + timeout
    url = f"{SITE_URL}/{slug}.html"
    while time.time() < deadline:
        build = json.loads(
            subprocess.run(
                ["gh", "api", PAGES_API], check=True, capture_output=True, text=True
            ).stdout
        )
        if build["status"] == "built":
            # Cache-bust so we see the fresh deploy, not the CDN's copy.
            req = urllib.request.Request(f"{url}?v={int(time.time())}")
            try:
                with urllib.request.urlopen(req) as resp:
                    if title.split(".")[0] in resp.read().decode():
                        return True
            except urllib.error.HTTPError:
                pass
        time.sleep(10)
    return False


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("markdown", type=Path)
    ap.add_argument("--desc", default="", help="index.html blurb for a new article")
    ap.add_argument("--no-push", action="store_true", help="render only")
    args = ap.parse_args()

    md_path = args.markdown.resolve()
    slug = md_path.stem
    title, page = render(md_path)
    out = REPO_DIR / f"{slug}.html"
    out.write_text(page)
    print(f"rendered {out.name}: {title}")

    added = ensure_index_entry(slug, title, args.desc or slug.replace("-", " "))
    if added:
        print("added index.html entry" + ("" if args.desc else " (edit the blurb!)"))

    if args.no_push:
        return

    status = git("status", "--porcelain", capture_output=True, text=True).stdout
    if not status.strip():
        print("nothing changed; skipping commit")
    else:
        git("add", f"{slug}.html", f"{slug}.md", "index.html")
        git("commit", "-m", f"Publish render: {title}")
        git("push")

    print("waiting for GitHub Pages build...")
    live = wait_for_pages(slug, title)
    canonical = f"{SITE_URL}/{slug}.html"
    print()
    print(f"canonical: {canonical}" + ("" if live else "  (build not confirmed yet — check manually)"))
    print(f"import at: https://medium.com/p/import  (paste the canonical URL)")


if __name__ == "__main__":
    main()
