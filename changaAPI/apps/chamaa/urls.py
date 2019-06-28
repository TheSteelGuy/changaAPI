from django.urls import path

from .views import UserChamaaView

urlpatterns = [
    path('groups/user/', UserChamaaView.as_view(), name='chamaa')
]