from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [


    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('pin.urls')),
    url(r'^accounts/', include('accounts.urls')),

]
