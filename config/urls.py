from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView

from home.views import home
from catalog.views import catalog_home
from club.views import club_home
from samples.views import packs_home
from profiles.views import signup

urlpatterns = [
    path("admin/", admin.site.urls),

    # Auth
    path(
        "accounts/login/",
        LoginView.as_view(
            template_name="registration/login.html",
            redirect_authenticated_user=True,
        ),
        name="login",
    ),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/signup/", signup, name="signup"),

    # Site pages
    path("", home, name="home"),
    path("catalog/", catalog_home, name="catalog"),
    path("club/", club_home, name="club"),
    path("packs/", packs_home, name="packs"),
    path("poll/", include("polls.urls")),
    path("membership/", include("checkout.urls")),
]