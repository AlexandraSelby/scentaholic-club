from django.shortcuts import render

from django.shortcuts import render

def poll_home(request):
    return render(request, "polls/poll_home.html")
