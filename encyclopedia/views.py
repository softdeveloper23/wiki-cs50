from django.shortcuts import render, redirect

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

def search(request):
    query = request.GET.get('q', '')
    entries = util.list_entries()
    if query in entries:
        return redirect('entry', title=query)
    else:
        filtered_entries = [entry for entry in entries if query.lower() in entry.lower()]
        return render(request, "encyclopedia/search_results.html", {
            "entries": filtered_entries,
            "query": query
        })
