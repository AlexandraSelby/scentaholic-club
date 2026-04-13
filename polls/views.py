
from django.shortcuts import render
from .models import WeeklyPoll


def poll_home(request):
    active_poll = WeeklyPoll.objects.filter(is_active=True).order_by("-created_at").first()

    return render(
        request,
        "polls/poll_home.html",
        {"poll": active_poll},
    )