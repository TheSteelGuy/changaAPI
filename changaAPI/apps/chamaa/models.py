from django.db import models
# from ..contributions.models import Contribution


class Chamaa(models.Model):
    """model for giving paybills name/title"""
    title = models.CharField(default='New Group', max_length=64, unique=True, null=False)
    account_number = models.CharField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=100, default='0')

    REQUIRED_FIELDS = ['title', 'account_number']

    def __str__(self):
        return self.title
