from django.urls import path

from Dashboard.views import dashboard

urlpatterns = [
    path('', dashboard, name='dashboard'),
]