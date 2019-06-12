from django.db import models
from ..contributions.models import Contribution
from ..authentication.models import User


class Membership(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    group = models.ForeignKey(Contribution, on_delete=models.CASCADE)

    group_name = models.CharField(default='', max_length=64)

    business_shortcode = models.CharField(max_length=100)

    # A timestamp representing when this object was created.
    created_at = models.DateTimeField(auto_now_add=True)

    # A timestamp representing when this object was last updated.
    updated_at = models.DateTimeField(auto_now=True)
