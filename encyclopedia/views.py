from django.shortcuts import render

from . import util

def index(request, title):
    # If title is empty, return an error page
    entry = util.get_entry(title)
    if entry is None:
        return render(request, "encyclopedia/error.html", {
            "error": "Page not found"
        })
    else:
        # If title is not empty, return the entry page
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "entry": entry
        })
