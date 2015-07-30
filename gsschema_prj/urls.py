from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'gsschema.views.index', name='index'),
    url(r'^gsschema/', include('gsschema.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
