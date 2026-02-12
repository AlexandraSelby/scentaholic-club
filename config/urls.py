from django.contrib import admin
from django.urls import path

from home.views import home
from catalog.views import catalog_home
from club.views import club_home
from samples.views import packs_home
from polls.views import poll_home
from checkout.views import membership_home

urlpatterns = [
    path("admin/", admin.site.urls),

    path("", home, name="home"),
    path("catalog/", catalog_home, name="catalog"),
    path("club/", club_home, name="club"),
    path("packs/", packs_home, name="packs"),
    path("poll/", poll_home, name="poll"),
    path("membership/", membership_home, name="membership"),
]
