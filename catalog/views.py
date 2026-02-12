from django.shortcuts import render

from django.shortcuts import render

def catalog_home(request):
    return render(request, "catalog/catalog_home.html")

