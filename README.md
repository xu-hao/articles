# articles

Rendered HTML copies of articles, hosted for canonical links and imports.
Drafts live elsewhere; anything here is published or about to be.

## Publishing to Medium

Medium no longer issues API integration tokens, so publishing goes through
GitHub Pages plus Medium's import tool:

```
./publish.py my-article.md --desc "one-line blurb for the index"
```

This renders the markdown with the shared page template, adds an index.html
entry if the article is new, commits and pushes, waits for the Pages build,
and prints the canonical URL to paste into https://medium.com/p/import
(the import tool sets the canonical link automatically). Use `--no-push` to
just render locally.

After publishing on Medium, add the "on Medium" link to the article's
index.html entry by hand.
