from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry, name="entry"),
    path("search", views.search, name="search"),
    path("create_new_page", views.new_page, name="new_page"),
    path("edit/<str:title>", views.edit_entry, name="edit_entry"),
    path("random", views.random_page, name="random_page")
]


