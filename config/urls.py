from django.contrib import admin
from django.urls import path, include

from home.views import home
from catalog.views import catalog_home
from club.views import club_home
from samples.views import packs_home
from polls.views import poll_home
from profiles.views import signup

urlpatterns = [
    
    path("admin/", admin.site.urls),

    # Auth
    path("accounts/", include("django.contrib.auth.urls")),

    # Site pages
    path("", home, name="home"),
    path("catalog/", catalog_home, name="catalog"),
    path("club/", club_home, name="club"),
    path("packs/", packs_home, name="packs"),
    path("poll/", poll_home, name="poll"),
    path("accounts/signup/", signup, name="signup"),
    path("membership/", include("checkout.urls")),
    
]