from django_filters.rest_framework import FilterSet
from django_filters import DateFromToRangeFilter
from .models import Trade


class TradeJournalFilter(FilterSet):
    created_at = DateFromToRangeFilter()

    class Meta:
        model = Trade
        fields = ['pair', 'session', 'entry_type',
                  'order_type', 'status', 'outcome']
