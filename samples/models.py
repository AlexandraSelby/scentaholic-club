from django.db import models
from catalog.models import Fragrance


class WeeklyPack(models.Model):
    title = models.CharField(max_length=120)
    week_start = models.DateField()
    week_end = models.DateField()
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-week_start"]

    def __str__(self):
        return f"{self.title} ({self.week_start} → {self.week_end})"


class PackItem(models.Model):
    pack = models.ForeignKey(WeeklyPack, on_delete=models.CASCADE, related_name="items")
    fragrance = models.ForeignKey(Fragrance, on_delete=models.PROTECT, related_name="pack_items")
    sample_size_ml = models.PositiveIntegerField(default=2)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["pack", "fragrance"], name="unique_pack_fragrance")
        ]

    def __str__(self):
        return f"{self.pack}: {self.fragrance} ({self.sample_size_ml}ml)"