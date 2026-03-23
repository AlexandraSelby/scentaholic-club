from django.db import models
from django.contrib.auth.models import User
from catalog.models import Fragrance


class WeeklyPoll(models.Model):
    title = models.CharField(max_length=120)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    poll = models.ForeignKey(WeeklyPoll, on_delete=models.CASCADE)
    fragrance = models.ForeignKey(Fragrance, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("user", "poll", "fragrance")

    def __str__(self):
        return f"{self.user} voted for {self.fragrance}"