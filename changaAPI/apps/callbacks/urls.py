from django.urls import path


from .lipa_na_mpesa import LipaNaMpesaView, MpesaValidationUrl

urlpatterns = [
    path(
        'c2b_confirm/',
        LipaNaMpesaView.as_view(),
        name='c2b_confirm'
    ),
    path('c2b_validation/', MpesaValidationUrl.as_view(), name='c2b_validation')
]
