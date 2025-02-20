from django.db import models
from users.models import UserAccount

# Create your models here.


class Trade(models.Model):
    """Model for create, update, delete, and get trades"""
    user = models.ForeignKey(
        UserAccount, on_delete=models.CASCADE, related_name="trades")
    pair = models.CharField(max_length=100, blank=False,
                            null=False)
    session = models.CharField(max_length=100, blank=True, default="")
    general_market_condition = models.CharField(
        max_length=100, blank=False, null=False)
    intermediate_market_condition = models.CharField(
        max_length=100, blank=False, null=False)
    entry_market_condition = models.CharField(
        max_length=100, blank=False, null=False)
    entry_strategy = models.CharField(
        max_length=255, blank=False, null=False)
    trade_entry_description = models.CharField(
        max_length=255, blank=True, null=True)
    entry_price = models.DecimalField(
        max_digits=10, decimal_places=5, blank=False, null=False)
    stoploss_price = models.DecimalField(
        max_digits=10, decimal_places=5, blank=False, null=False)
    entry_type = models.CharField(max_length=100, blank=False, null=False)
    order_type = models.CharField(
        max_length=100, blank=False, null=False, default="market execution")
    status = models.CharField(max_length=100, blank=False, null=False)
    outcome = models.CharField(max_length=100, blank=False, null=False)
    manual_exit_reason = models.CharField(
        max_length=255, blank=True, null=True)
    image_url = models.URLField(max_length=255, blank=True, null=True)
    time_executed = models.DateTimeField(blank=True, null=True)
    trade_duration = models.PositiveSmallIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Trade {self.id} - {self.pair} ({self.entry_strategy})"


class ProfitTarget(models.Model):
    """Profit targets linked to a trade"""
    trade = models.ForeignKey(
        Trade, on_delete=models.CASCADE, related_name="profit_targets"
    )
    target = models.DecimalField(max_digits=10, decimal_places=5)

    def __str__(self):
        return f"Profit Target {self.target} for Trade {self.trade.id}"
