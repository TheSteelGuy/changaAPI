from rest_framework import generics, permissions, status

from rest_framework.response import Response


from .serializers import ContributionSerializer
from .models import Contribution
from ..authentication.models import User


class ContributionView(generics.ListAPIView):
    """Load contributions bu a user"""
    permission_classes = (permissions.IsAuthenticated,)

    serializer_class = ContributionSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = User.objects.filter(phone_number__contains=user).first().contributions.all()
        return queryset


class ContributionAllView(generics.ListAPIView):
    """Load contributions for  all users"""
    permission_classes = (permissions.IsAuthenticated,)

    serializer_class = ContributionSerializer

    queryset = Contribution.objects.all()








