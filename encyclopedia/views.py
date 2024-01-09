import random
import markdown2
from django.shortcuts import render, redirect
from .models import NewEntryForm
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    entry_content = util.get_entry(title)
    if entry_content is None:
        return render(request, "wiki/error.html", {
            "message": "The requested page was not found."
        })
    else:
        html_content = markdown2.markdown(entry_content)
        return render(request, "wiki/entry.html", {
            "title": title,
            "entry": html_content
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

def new_page(request):
    if request.method == "POST":
        form = NewEntryForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            if util.get_entry(title) is not None:
                # An entry with this title already exists
                return render(request, "wiki/error.html", {
                    "message": "An encyclopedia entry with this title already exists."
                })
            else:
                util.save_entry(title, content)
                return redirect("entry", title=title)
    else:
        return render(request, "encyclopedia/create_new_page.html", {
            "form": NewEntryForm()
        })

def edit_entry(request, title):
    if request.method == "POST":
        content = request.POST['content']
        util.save_entry(title, content)
        return redirect('entry', title=title)
    else:
        content = util.get_entry(title)
        if content is None:
            return render(request, "wiki/error.html", {
                "message": "The requested page was not found."
            })
        else:
            return render(request, "wiki/edit_entry.html", {
                "title": title,
                "content": content
            })

def random_page(request):
    entries = util.list_entries()
    random_title = random.choice(entries)
    return redirect('entry', title=random_title)