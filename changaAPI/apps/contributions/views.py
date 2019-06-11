from rest_framework import generics, permissions, status

from rest_framework.response import Response


from .serializers import ContributionSerializer
from .models import Contribution


class ContributionView(generics.ListAPIView):
    """Register a new user """
    queryset = Contribution.objects.all()
    #permission_classes = (permissions.IsAuthenticated,)

    permission_classes = (permissions.AllowAny,)

    serializer_class = ContributionSerializer






