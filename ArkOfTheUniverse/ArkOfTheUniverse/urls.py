from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', include('Dashboard.urls')),
    path('web3/', include('BlockchainSystem.urls')),
    path('server/', include('SecuritySystem.urls')),
    path('game/api/', include('GameAPI.urls')),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]

admin.site.site_header = "ArkOfTheUniverse Admin"
admin.site.site_title = "ArkOfTheUniverse Admin Portal"
admin.site.index_title = "Welcome to ArkOfTheUniverse Portal"