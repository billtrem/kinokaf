from django.shortcuts import render
from .models import LandingAsset

def home(request):
    asset = LandingAsset.objects.last()
    return render(request, "main/index.html", {"asset": asset})
