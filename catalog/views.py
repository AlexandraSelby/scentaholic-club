from django.shortcuts import render
from .models import Fragrance


def catalog_home(request):
    fragrances = Fragrance.objects.all()
    return render(
        request,
        "catalog/catalog_home.html",
        {"fragrances": fragrances}
    )