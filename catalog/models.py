from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=120, unique=True)
    country = models.CharField(max_length=80, blank=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Fragrance(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name="fragrances")
    name = models.CharField(max_length=150)
    year_released = models.PositiveIntegerField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["brand__name", "name"]
        constraints = [
            models.UniqueConstraint(fields=["brand", "name"], name="unique_brand_fragrance_name")
        ]

    def __str__(self):
        return f"{self.brand} — {self.name}"