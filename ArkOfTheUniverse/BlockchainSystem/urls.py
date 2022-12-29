from django.urls import path

from BlockchainSystem.views import moralis_auth, moralis_logout , RequestMessage, VerifyMessage

urlpatterns = [
    path('connect', moralis_auth, name='login'),
    path('disconnect', moralis_logout, name='logout'),
    path('request_message', RequestMessage, name='request_message'),
    path('verify_message', VerifyMessage, name='verify_message')
]