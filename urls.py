from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from rh.views import index

urlpatterns = patterns('',

    url(r'^$', index),
    url(r'^api/', include('rh.api.urls')),
    url(r'^servidor/', include('rh.servidor.urls')),
    # Examples:
    # url(r'^$', 'rh.views.home', name='home'),
    # url(r'^rh/', include('rh.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
