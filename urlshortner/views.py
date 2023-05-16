"""Base views for home page."""
from django.shortcuts import render


def index(request):
    """Basic get method to return home page."""
    return render(request,"home.html")