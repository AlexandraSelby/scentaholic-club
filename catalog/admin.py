from django.contrib import admin
from .models import Brand, Fragrance


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    list_display = ["name", "country"]


@admin.register(Fragrance)
class FragranceAdmin(admin.ModelAdmin):
    search_fields = ["name", "brand__name"]
    list_filter = ["brand", "is_active"]
    list_display = ["name", "brand", "year_released", "is_active"]
