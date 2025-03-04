from django.db import models
from users.models import UserAccount

# Create your models here.


class Trade(models.Model):
    """Model for create, update, delete, and get trades"""
    user = models.ForeignKey(
        UserAccount, on_delete=models.CASCADE, related_name="trades")
    pair = models.CharField(max_length=100, blank=False,
                            null=False)
    session = models.CharField(max_length=100, blank=True, null=True)
    entry_type = models.CharField(max_length=100, blank=False, null=False)
    order_type = models.CharField(
        max_length=100, blank=False, null=False)
    entry_price = models.DecimalField(
        max_digits=10, decimal_places=5, blank=False, null=False)
    stoploss_price = models.DecimalField(
        max_digits=10, decimal_places=5, blank=False, null=False)
    risk_reward_ratio = models.FloatField(null=True, blank=True)
    trade_duration = models.PositiveIntegerField(
        blank=True, null=True)  # Trade duration in minutes
    status = models.CharField(max_length=50, choices=[
                              ("Open", "Open"), ("Closed", "Closed")])
    outcome = models.CharField(max_length=50, choices=[(
        "Profit", "Profit"), ("Loss", "Loss"), ("Breakeven", "Breakeven")])
    execution_time = models.DateTimeField(blank=True, null=True)
    trade_description = models.CharField(
        max_length=255, blank=True, null=True)
    image_url = models.URLField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Trade {self.id} - {self.pair} {self.entry_type} ({self.status})"


class ProfitTarget(models.Model):
    """Profit targets linked to a trade"""
    trade = models.ForeignKey(
        Trade, on_delete=models.CASCADE, related_name="profit_targets"
    )
    target = models.DecimalField(max_digits=10, decimal_places=5)

    def __str__(self):
        return f"Profit Target {self.target} for Trade {self.trade.id}"
