from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'borrowing/', include('borrowing.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
