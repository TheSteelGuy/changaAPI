from rest_framework import serializers

from .models import Chamaa


class ChamaaSerializer(serializers.ModelSerializer):
    """Chamaa serializer"""
    title = serializers.CharField()
    account_number = serializers.CharField()
    required_amount = serializers.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        model = Chamaa
        fields = ['title', 'account_number', 'required_amount']
