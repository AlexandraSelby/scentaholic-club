from django.shortcuts import render

from django.shortcuts import render

def club_home(request):
    return render(request, "club/club_home.html")
