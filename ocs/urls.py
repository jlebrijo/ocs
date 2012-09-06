from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'ocs.views.home', name='home'),
    url(r'^validate$', 'ocs.views.validate', name='validate'),
    url(r'^authenticate$', 'ocs.views.authenticate', name='authenticate'),
    url(r'^survey_done$', 'ocs.views.survey_done', name='survey_done'),
    # url(r'^ocs/', include('ocs.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
