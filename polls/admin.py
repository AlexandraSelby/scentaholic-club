from django.contrib import admin
from .models import WeeklyPoll, Vote


@admin.register(WeeklyPoll)
class WeeklyPollAdmin(admin.ModelAdmin):
    list_display = ["title", "is_active", "created_at"]


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ["user", "poll", "fragrance"]
    list_filter = ["poll"]