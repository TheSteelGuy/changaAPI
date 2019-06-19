from django.urls import path

from .views import ContributionView, ContributionAllView

urlpatterns = [
    path('contributions/user/', ContributionView.as_view(), name='user_contribution'),
    path('contributions/', ContributionAllView.as_view(), name='all_contribution')
]
