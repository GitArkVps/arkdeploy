from django.urls import path

from GameAPI.views import MiningGenerate, MiningClaim, PlayerElements, ShipDetails

urlpatterns = [
    path('mining/generate', MiningGenerate),
    path('mining/claim', MiningClaim),
    path('player/elements', PlayerElements),
    path('ship/details', ShipDetails),
]