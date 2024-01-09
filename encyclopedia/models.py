from django.db import models
from django import forms

# Create your models here.
class NewEntryForm(forms.Form):
    title = forms.CharField(label="Title", max_length=100)
    content = forms.CharField(widget=forms.Textarea, label="Content")