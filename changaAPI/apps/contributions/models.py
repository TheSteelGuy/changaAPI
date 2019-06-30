from django.db import models
from ..constants.models import MAX_DECIMAL_POINTS


class Contribution(models.Model):

    transaction_type = models.CharField(default='', max_length=255)

    transaction_id = models.CharField(max_length=255, unique=True)

    amount = models.DecimalField(max_digits=MAX_DECIMAL_POINTS, decimal_places=2)

    business_shortcode = models.CharField(max_length=255, default='0')

    bill_ref_number = models.CharField(default='', max_length=255)

    account_balance = models.CharField(max_length=255)

    msisdn = models.CharField(max_length=255)

    first_name = models.CharField(max_length=255)

    middle_name = models.CharField(max_length=255)

    last_name = models.CharField(max_length=255)
    
    required_amount = models.DecimalField(max_digits=MAX_DECIMAL_POINTS, decimal_places=2, default=0.00)

    # A timestamp representing when this object was created.
    created_at = models.DateTimeField(auto_now_add=True)

    # A timestamp representing when this object was last updated.
    updated_at = models.DateTimeField(auto_now=True)

    REQUIRED_FIELDS = ['amount', 'transaction_id', 'transaction_id', 'chamaa']

    def __str__(self):
        """
        Returns a string representation of this `User`.
        This string is used when a `User` is printed in the console.
        """
        return 'Transaction Id: {} | Amount: {}'.format(self.transaction_id, self.amount)



