from django.conf.urls import include, url
from django.contrib import admin

from borrowing import views

urlpatterns = [
    url(r'^$', views.redirect_to_borrowing),
    url(r'^borrowing/', include('borrowing.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
