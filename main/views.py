from django.shortcuts import render
from .models import LandingAsset


def home(request):
    """
    Homepage — displays latest LandingAsset (title, description, Cloudinary image).
    """
    asset = LandingAsset.objects.order_by("-created_at").first()
    return render(request, "main/index.html", {"asset": asset})


def cinema(request):
    """
    Cinema page.
    """
    return render(request, "main/cinema.html")


def cafe(request):
    """
    Cafe & Bar page.
    """
    return render(request, "main/cafe.html")


def library(request):
    """
    Loan Library page.
    """
    return render(request, "main/library.html")


def gigs(request):
    """
    Gigs page — live music, comedy, spoken word, theatre.
    """
    return render(request, "main/gigs.html")


def info(request):
    """
    General information page — opening times, location, contact.
    """
    return render(request, "main/info.html")
