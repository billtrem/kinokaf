from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("cinema/", views.cinema, name="cinema"),
    path("cafe/", views.cafe, name="cafe"),
    path("library/", views.library, name="library"),
    path("info/", views.info, name="info"),
    path("gigs/", views.gigs, name="gigs"),   # NEW
]
