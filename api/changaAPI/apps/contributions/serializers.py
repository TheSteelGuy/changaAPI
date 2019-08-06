from rest_framework import serializers
from django.core.validators import RegexValidator
from .models import Contribution


class ContributionSerializer(serializers.ModelSerializer):
    """Contribution Serialization class."""

    transaction_type = serializers.CharField(max_length=255)

    transaction_id = serializers.CharField(max_length=255)

    amount = serializers.DecimalField(max_digits=10, decimal_places=2)

    business_shortcode = serializers.CharField(max_length=255)

    bill_ref_number = serializers.CharField( max_length=255)

    account_balance = serializers.CharField(max_length=255)

    msisdn = serializers.CharField(max_length=255)

    first_name = serializers.CharField(max_length=255)
    middle_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)
    required_amount = serializers.DecimalField(max_digits=10, decimal_places=2)

    indicator_level = serializers.DecimalField(max_digits=3, decimal_places=2)

    outstanding_balance = serializers.DecimalField(max_digits=10, decimal_places=2)

    # A timestamp representing when this object was created.
    created_at = serializers.DateTimeField()
    class Meta:
        model = Contribution
        # List all of the fields that could possibly be included in a request
        # or response, including fields specified explicitly above.
        fields = ['transaction_type', 'transaction_id', 'amount', 'business_shortcode', 'bill_ref_number',
                  'account_balance', 'msisdn', 'first_name', 'middle_name', 'last_name','required_amount', 'indicator_level','outstanding_balance', 'created_at']
