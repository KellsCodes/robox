from rest_framework import serializers

from .models import Trade, ProfitTarget


class ProfitTargetSerializer(serializers.ModelSerializer):
    """Serialize for profit targets"""

    class Meta:
        model = ProfitTarget
        fields = ["target"]


class TradeSerializer(serializers.ModelSerializer):
    """Trade model serializer"""
    profit_targets = ProfitTargetSerializer(many=True)

    class Meta:
        model = Trade
        # fields = "__all__"
        exclude = ["user"]

    def create(self, validated_data):
        """Create trade and it's profit targets"""
        profit_targets_data = validated_data.pop("profit_targets", [])
        trade = Trade.objects.create(**validated_data)

        # Create related profit targets
        for target_data in profit_targets_data:
            ProfitTarget.objects.create(trade=trade, **target_data)

        return trade

    def update(self, instance, validated_data):
        """Update trade and handle profit targets"""
        profit_targets_data = validated_data.pop("profit_targets", None)
        print(f"profit_targets_data: {profit_targets_data}")

        # Update trade fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        # Update trade fields
        if profit_targets_data is not None:
            instance.profit_targets.all().delete()
            for target_data in profit_targets_data:
                ProfitTarget.objects.create(trade=instance, **target_data)

        return instance
