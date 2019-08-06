import os
from rest_framework import generics, permissions, status

from rest_framework.response import Response


from .serializers import ContributionSerializer
from .models import Contribution
from ..authentication.models import User
from ..chamaa.models import Chamaa

from ..helpers.stk_push_password import construct_password
from ..constants.views import (
    TRANSACTIONTYPE, TRANSACTIONDESC, ACCOUNTREF,CONTRIBUTION_MESSAGE,
    SERVER_ERROR
    )
from ..helpers.contribution_request import send_request


class UserContributionByAccountNumberView(generics.ListAPIView):
    """Load contributions bu a user"""
    permission_classes = (permissions.IsAuthenticated,)

    serializer_class = ContributionSerializer

    def get_queryset(self):
        user = self.request.user
        account_number = self.request.query_params.get('account-number', None)
     
        queryset= Chamaa.objects.filter(account_number=account_number).first().contributions.all()

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


class MakeContribution(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Contribution.objects.all()
    def post(self, request, **kwargs):
        try:
            bussiness_shortcode = request.data["BusinessShortCode"]
            password, timestamp = construct_password(bussiness_shortcode)
          
            amount = request.data["Amount"]
            phone_number = '254' + str(self.request.user.phone_number)
            party_b = bussiness_shortcode 
            party_a = phone_number

            contribution_obj = dict(
                BusinessShortCode=bussiness_shortcode,
                Password=password,
                Timestamp=timestamp,
                TransactionType=TRANSACTIONTYPE,
                Amount=amount,
                PartyA=party_a,
                PartyB=party_b,
                PhoneNumber=phone_number,
                CallBackURL=os.environ["CALLBACK_URL"],
                AccountReference=ACCOUNTREF,
                TransactionDesc=TRANSACTIONDESC.format(bussiness_shortcode)
            )
            res=send_request(contribution_obj)#send request
            print(contribution_obj)
        
            return Response({'message':CONTRIBUTION_MESSAGE.format(amount)},status=status.HTTP_200_OK)
        except Exception as e:
            # log error
            # print(e)
            return Response({'message':SERVER_ERROR}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)









