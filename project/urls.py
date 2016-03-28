from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^$', 'calc.views.say_main',),
    url(r'^(\d+)(\+)(\d+)$', 'calc.views.suma',),
    url(r'^(\d+)(\-)(\d+)$', 'calc.views.resta',),
    url(r'^(\d+)(\*)(\d+)$', 'calc.views.multiplica',),
    url(r'^(\d+)(\/)(\d+)$', 'calc.views.divide',),
    url(r'^.*$', 'calc.views.error',),
    url(r'^admin/', include(admin.site.urls)),
)
