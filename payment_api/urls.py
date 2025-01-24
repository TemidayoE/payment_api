from django.urls import path
from payment_api.views import InitializePaymentView, VerifyPaymentView

urlpatterns = [
    path('initialize-payment/', InitializePaymentView.as_view(), name='initialize-payment'),
    path('verify-payment/<str:reference>/', VerifyPaymentView.as_view(), name='verify-payment'),
]

