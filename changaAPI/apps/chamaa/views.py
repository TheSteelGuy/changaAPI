from django.shortcuts import render
from rest_framework import generics, permissions, status
from .models import Chamaa

from .serializers import ChamaaSerializer


class UserChamaaView(generics.ListAPIView):
    """Fetch user chamas"""
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ChamaaSerializer

    def get_queryset(self):
        user = self.request.user
        
        queryset = Chamaa.objects.filter(phone_number__contains=user.phone_number).all()
        return queryset
