from django.shortcuts import render
from .models import WeeklyPack


def packs_home(request):
    packs = WeeklyPack.objects.filter(is_published=True)

    return render(
        request,
        "samples/packs_home.html",
        {"packs": packs}
    )