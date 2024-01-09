from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    entry = util.get_entry(title)
    if entry is None:
        return render(request, "wiki/error.html", {
            "message": "The requested page was not found."
        })
    else:
        return render(request, "wiki/entry.html", {
            "title": title,
            "entry": entry
        })

