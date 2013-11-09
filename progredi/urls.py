from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^progress/', include('progress.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
