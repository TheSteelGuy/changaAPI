from rest_framework import generics, permissions, status

from rest_framework.response import Response


from .serializers import ContributionSerializer
from .models import Contribution
from ..authentication.models import User
from ..chamaa.models import Chamaa


class UserContributionByAccountNumberView(generics.ListAPIView):
    """Load contributions bu a user"""
    permission_classes = (permissions.IsAuthenticated,)

    serializer_class = ContributionSerializer

    def get_queryset(self):
        user = self.request.user
        account_number = self.request.query_params.get('account-number', None)
        import pdb;pdb.set_trace()
        print(account_number)

        chamaa = Chamaa.objects.filter(account_number=account_number, ).first()

        queryset = Contribution.objects.filter(chamaa=chamaa).all()

        return queryset


class ContributionUserView(generics.ListAPIView):
    """Load contributions bu a user"""
    permission_classes = (permissions.IsAuthenticated,)

    serializer_class = ContributionSerializer

    def get_queryset(self):
        user = self.request.user
        account_number = self.request.query_params.get('account-number', None)
        queryset = None
        if account_number:
            queryset = Contribution.objects.filter(msisdn__contains=user, business_shortcode=account_number).all()
        else:
            queryset = Contribution.objects.filter(msisdn__contains=user).all()

        return queryset


class ContributionAllView(generics.ListAPIView):
    """Load contributions for  all users"""
    permission_classes = (permissions.IsAuthenticated,)

    serializer_class = ContributionSerializer

    queryset = Contribution.objects.all()








