from django.urls import path
from .views import poll_home, delete_vote

urlpatterns = [
    path("", poll_home, name="poll"),
    path("delete/", delete_vote, name="delete_vote"),
]