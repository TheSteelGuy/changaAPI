from django.urls import path

from .views import ContributionView

urlpatterns = [
    path('contributions/', ContributionView.as_view(), name='contribution')
]
