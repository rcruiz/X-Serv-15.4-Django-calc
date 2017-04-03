from django.conf.urls import patterns, include, url
from django.contrib import admin
from calc import views

urlpatterns = [
    url(r'^(\d+)(\+)(\d+)$', views.suma),
    url(r'^(\d+)(\-)(\d+)$', views.resta),
    url(r'^(\d+)(\*)(\d+)$', views.multiplica),
    url(r'^(\d+)(\/)(\d+)$', views.divide),
    url(r'^.*$', views.el404),
    url(r'^admin/', include(admin.site.urls)),
]
