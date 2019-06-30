from django.shortcuts import render
from rest_framework import generics, permissions, status
from ..authentication.models import User

from .serializers import ChamaaSerializer


class UserChamaaView(generics.ListAPIView):
    """Fetch user chamas"""
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ChamaaSerializer

    def get_queryset(self):
        user = self.request.user
        
        queryset = User.objects.filter(phone_number__contains=user.phone_number).first().chamaas.all()
        return queryset
