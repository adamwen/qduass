from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     url(r'^auth$', 'ass.views.authorization', name='auth'),
     url(r'^index$', 'ass.views.index', name='index'),
     url(r'^send$', 'ass.views.send', name='send'),
     url(r'^refresh_accesstoken', 'ass.views.refresh_accesstoken', name='refresh_accesstoken'),
    # url(r'^qduass/', include('qduass.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
