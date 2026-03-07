from django.conf import settings
from django.db import models


class Game(models.Model):
    title = models.CharField(max_length=120)
    platform = models.CharField(max_length=60, blank=True)
    genre = models.CharField(max_length=60, blank=True)
    price_per_rental = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    is_active = models.BooleanField(default=True)
    cover_url = models.URLField(blank=True, null=True)

    def __str__(self) -> str:
        return self.title


class Plan(models.Model):
    name = models.CharField(max_length=80)
    monthly_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name


class Rental(models.Model):
    RENTAL_TYPE_CHOICES = [
        ("INDIVIDUAL", "Individual"),
        ("PLAN", "Plan"),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.SET_NULL, null=True, blank=True)

    rental_type = models.CharField(max_length=12, choices=RENTAL_TYPE_CHOICES, default="INDIVIDUAL")
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(null=True, blank=True)
    is_returned = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.user} - {self.game} ({self.rental_type})"