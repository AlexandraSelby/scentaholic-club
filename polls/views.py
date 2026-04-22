from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import VoteForm
from .models import Vote, WeeklyPoll


@login_required
def poll_home(request):
    poll = WeeklyPoll.objects.filter(is_active=True).order_by("-created_at").first()

    if not poll:
        return render(request, "polls/poll_home.html", {"poll": None})

    existing_votes = Vote.objects.filter(user=request.user, poll=poll)
    has_voted = existing_votes.exists()

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

            messages.success(request, "Your vote has been successfully submitted.")
            return redirect("poll")
    else:
        form = VoteForm(poll=poll)

    return render(
        request,
        "polls/poll_home.html",
        {
            "poll": poll,
            "form": form,
            "has_voted": has_voted,
            "existing_votes": existing_votes,
        },
    )
@login_required
def delete_vote(request):
    poll = WeeklyPoll.objects.filter(is_active=True).order_by("-created_at").first()

    if poll and request.method == "POST":
        Vote.objects.filter(user=request.user, poll=poll).delete()
        messages.success(request, "Your vote has been removed.")

    return redirect("poll")