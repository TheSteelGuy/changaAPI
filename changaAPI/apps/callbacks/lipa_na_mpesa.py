from rest_framework.response import Response
from rest_framework import generics, permissions, status
from ..authentication.models import User

from ..chamaa.models import Chamaa


from ..contributions.models import Contribution


class LipaNaMpesaView(generics.CreateAPIView):
    """callback for mpesa response """
    permission_classes = (permissions.AllowAny,)

    def post(self, request, **kwargs):
        print('....................................................................≥≥...................')
        phone = request.data.get('MSISDN')
        phone_number = phone if len(phone) <= 10 else phone[3:]

        chamaa_obj = Chamaa.objects.filter(account_number=request.data.get('BusinessShortCode')).first()

        if not chamaa_obj:
            chamaa_obj = Chamaa.objects.create(
                title='chamaa'+request.data.get('BusinessShortCode'),
                account_number=request.data.get('BusinessShortCode'),
            )
  

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
            last_name=request.data.get('LastName'),
            required_amount = chamaa_obj.required_amount
        )

        contribution_obj.save()

        user = User.objects.filter(phone_number__contains=phone_number).first()

        if not user:
            user = User.objects.create_user(
                phone_number=phone_number,
                username='user'+phone_number,
                password=phone_number
            )

        user.contributions.add(contribution_obj)


        chamaa_obj.contributions.add(contribution_obj)
        user.chamaas.add(chamaa_obj)


        print(contribution_obj)

        return Response({'message': request.data}, status=status.HTTP_200_OK)


class MpesaValidationUrl(generics.CreateAPIView):
    """callback for validation"""
    permission_classes = (permissions.AllowAny,)

    def post(self, request, **kwargs):
        print('>>>>>>>>>>>>>>'*15)
        print(request.data)

        return Response(status=status.HTTP_200_OK)
