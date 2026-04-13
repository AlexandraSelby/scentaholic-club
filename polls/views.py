from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import VoteForm
from .models import Vote, WeeklyPoll


@login_required
def poll_home(request):
    poll = WeeklyPoll.objects.filter(is_active=True).order_by("-created_at").first()

    if not poll:
        return render(request, "polls/poll_home.html", {"poll": None})

    if request.method == "POST":
        form = VoteForm(request.POST, poll=poll)
        if form.is_valid():
            selected_fragrances = form.cleaned_data["fragrances"]

            Vote.objects.filter(user=request.user, poll=poll).delete()

            for fragrance in selected_fragrances:
                Vote.objects.create(
                    user=request.user,
                    poll=poll,
                    fragrance=fragrance,
                )

            return redirect("poll")
    else:
        form = VoteForm(poll=poll)

    return render(
        request,
        "polls/poll_home.html",
        {
            "poll": poll,
            "form": form,
        },
    )