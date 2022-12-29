from SecuritySystem.views import GenerateConnection, ConnectWallet, CheckConnection, CheckStatus, ShipSelection, ShipConfirmation
from django.urls import path

from . import views

urlpatterns = [
    path('generate_connection/', GenerateConnection),
    path('check_connection/', CheckConnection),
    path('connect/<str:key_connection>', ConnectWallet),
    path('status/', CheckStatus),
    path('ShipSelection/', ShipSelection, name='ShipSelection'),
    path('ShipConfirmation/<str:ShipID>', ShipConfirmation, name='ShipConfirmation'),
]