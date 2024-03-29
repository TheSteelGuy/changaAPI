import os
from rest_framework import generics, permissions, status

from rest_framework.response import Response
import uuid
from datetime import date

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
from decimal import Decimal


class UserContributionByAccountNumberView(generics.ListAPIView):
    """Load contributions bu a user"""
    permission_classes = (permissions.IsAuthenticated,)

    serializer_class = ContributionSerializer

    def get_queryset(self):
        user = self.request.user
        account_number = self.request.query_params.get('account-number', None)
     
        queryset = Chamaa.objects.filter(account_number=account_number).first().contributions.all()

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

            contribution_dict = dict(
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

            res = send_request(contribution_dict)# send request
            try:
                if res['ResponseCode'] == '0':
                    contribution = Contribution.objects.filter(
                    msisdn=phone_number,
                    business_shortcode=bussiness_shortcode,
                    created_at__month=date.today().month
                    ).first()
                    if not contribution:
                        contribution_obj = Contribution(
                            transaction_type=TRANSACTIONTYPE,

                            transaction_id=str(uuid.uuid4()),

                            business_shortcode=bussiness_shortcode,
                            account_balance='0.00',

                            msisdn=phone_number,

                            checkout_request_id=res['CheckoutRequestID'],
                            merchant_request_id=res['MerchantRequestID'],
                            last_amount=Decimal(amount),
                            password=password,
                            timestamp=timestamp
                        )

                        contribution_obj.save()
                        return Response({'message': CONTRIBUTION_MESSAGE.format(amount)},status=status.HTTP_200_OK)
                    else:
                        contribution.checkout_request_id = res['CheckoutRequestID']
                        contribution.save() 
                        return Response({'message': CONTRIBUTION_MESSAGE.format(amount)},status=status.HTTP_200_OK)
            except KeyError:
                return Response({'message': 'Another tranascation is still ongoing, complete it first. Thanks'},status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            raise e
            return Response({'message': SERVER_ERROR}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)









