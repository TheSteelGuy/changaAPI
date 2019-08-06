from django.urls import path

from .views import (UserContributionByAccountNumberView, ContributionAllView,
 ContributionUserView, MakeContribution)

urlpatterns = [
    path('contributions/short-code/', UserContributionByAccountNumberView.as_view(), name='user_contribution'),
    path('contributions/all/', ContributionAllView.as_view(), name='all_contribution'),
    path('contributions/user/', ContributionUserView.as_view(), name='contributions'),
    path('contribute/', MakeContribution.as_view(), name='contribute')
]
