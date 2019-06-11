from rest_framework.response import Response
from rest_framework import generics, permissions, status

#models

from ..contributions.models import Contribution


class LipaNaMpesaView(generics.CreateAPIView):
    """callback for mpesa response """
    permission_classes = (permissions.AllowAny,)

    def post(self, request, **kwargs):
        print('....................................................................≥≥...................')

        contribution_obj = Contribution(
            transaction_type=request.data.get('TransactionType'),

            transaction_id=request.data.get('TransID'),

            amount=request.data.get('TransAmount'),

            business_shortcode=request.data.get('BusinessShortCode'),

            bill_ref_number=request.data.get('BillRefNumber'),

            account_balance=request.data.get('OrgAccountBalance'),

            msisdn=request.data.get('MSISDN'),

            first_name=request.data.get('FirstName'),
            middle_name=request.data.get('MiddleName'),
            last_name=request.data.get('LastName')
        )

        contribution_obj.save()

        # impliment server sent to update UI

        print(request.data)

        return Response({'message': request.data}, status=status.HTTP_200_OK)


class MpesaValidationUrl(generics.CreateAPIView):
    """callback for validation"""
    permission_classes = (permissions.AllowAny,)

    def post(self, request, **kwargs):
        print('wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwnnnwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww')

        print(request.data)

        return Response('completed', status=status.HTTP_200_OK)
