from rest_framework import serializers

from .models import Chamaa


class ChamaaSerializer(serializers.ModelSerializer):
    """Chamaa serializer"""
    title = serializers.CharField()
    account_number = serializers.CharField()

    class Meta:
        model = Chamaa
        fields = ['title', 'account_number']
