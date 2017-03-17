from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name="borrowingindex"),
    url(r'summary/(?P<user_id>[0-9]+)/$', views.summary, name="summary"),
]