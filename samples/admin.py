from django.contrib import admin
from .models import WeeklyPack, PackItem


class PackItemInline(admin.TabularInline):
    model = PackItem
    extra = 1


@admin.register(WeeklyPack)
class WeeklyPackAdmin(admin.ModelAdmin):
    list_display = ["title", "week_start", "week_end", "is_published"]
    list_filter = ["is_published"]
    inlines = [PackItemInline]


@admin.register(PackItem)
class PackItemAdmin(admin.ModelAdmin):
    list_display = ["pack", "fragrance", "sample_size_ml"]
    list_filter = ["pack"]