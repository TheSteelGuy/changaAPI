from django.urls import path

from .views import UserContributionByAccountNumberView, ContributionAllView, ContributionUserView

urlpatterns = [
    path('contributions/short-code/', UserContributionByAccountNumberView.as_view(), name='user_contribution'),
    path('contributions/all/', ContributionAllView.as_view(), name='all_contribution'),
    path('contributions/user/', ContributionUserView.as_view(), name='contributions')
]
