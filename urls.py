from django.conf.urls.defaults import *
from django.contrib import admin
from django.contrib.flatpages import urls
admin.autodiscover()

urlpatterns = patterns('',
    # Dependancies - TinyMCE
    url(r'^tiny_mce(?P<path>.*)$', 'django.views.static.serve', { 'document_root': '/home/dan/Downloads/tinymce/jscripts/tiny_mce' }),
    # Admin
    url(r'^admin/', include(admin.site.urls)),
    # Search
    url(r'^search/$', 'cms.search.views.search'),
    # Weblog include
    url(r'^weblog/', include('gambino.urls')),
    # Contact
    url(r'^contactus/$', 'cms.search.views.contactus'),
    # Catch All
    url(r'', include('django.contrib.flatpages.urls')),
)
