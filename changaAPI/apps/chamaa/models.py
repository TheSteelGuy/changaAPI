from django.db import models
from ..contributions.models import Contribution
from ..constants.models import MAX_DECIMAL_POINTS


class Chamaa(models.Model):
    """model for giving paybills name/title"""
    title = models.CharField(default='New Group', max_length=64, unique=True, null=False)
    account_number = models.CharField(max_length=100, unique=True)
    contributions = models.ManyToManyField(Contribution, blank=True)
    required_amount = models.DecimalField(decimal_places=2, max_digits=10, default=0.00)
    REQUIRED_FIELDS = ['title', 'account_number']

    def __str__(self):
        return self.title

