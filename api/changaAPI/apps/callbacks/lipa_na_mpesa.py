from rest_framework.response import Response
from rest_framework import generics, permissions, status
from typing import Any
from decimal import Decimal

from ..authentication.models import User

from ..chamaa.models import Chamaa


from ..contributions.models import Contribution

from ..helpers.contribution_request import add_context_to_contribution


class LipaNaMpesaView(generics.CreateAPIView):
    """callback for mpesa response """
    permission_classes = (permissions.AllowAny,)

    def post(self, request, **kwargs):

        print('....................................................................≥≥...................')

        data = request.data.get('Body')

        # get the contribution to update
        contribution = Contribution.objects.filter(checkout_request_id=data['stkCallback']['CheckoutRequestID']).first()
        phone = str(data['stkCallback']['CallbackMetadata']['Item'][-1].get('Value'))
        phone_number = phone if len(phone) <= 10 else phone[3:]

        chamaa_obj = Chamaa.objects.filter(account_number=contribution.business_shortcode).first()


        # if not chamaa_obj:
        #     chamaa_obj = Chamaa.objects.create(
        #         title='chamaa' + contribution.business_shortcode,
        #         account_number=contribution.business_shortcode,
        #     )

        if data['stkCallback']['ResultCode'] == 0:
            callback_meta = data['stkCallback']['CallbackMetadata']['Item']  # type: Any

            contribution.transaction_id = callback_meta[1].get('Value')

            contribution.account_balance = callback_meta[2].get('Value', '0.00')

            contribution.amount += Decimal(str(callback_meta[0].get('Value')))

            contribution.required_amount = chamaa_obj.required_amount

            user = User.objects.filter(phone_number__contains=phone_number).first()

            if not user:
                user = User.objects.create_user(
                    phone_number=phone_number,
                    username='user'+phone_number,
                    password=phone_number
                )

            # calculations function
            add_context_to_contribution(contribution, chamaa_obj, user)

            return Response({'message': 'Thank you dear member, your contribution has been recorded'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Something went wrong your transaction was not completed'}, status=status.HTTP_400_BAD_REQUEST)


class MpesaValidationUrl(generics.CreateAPIView):
    """callback for validation"""
    permission_classes = (permissions.AllowAny,)

    def post(self, request, **kwargs):
        print('>>>>>>>>>>>>>>'*15)
        print(request.data)

        return Response(status=status.HTTP_200_OK)
