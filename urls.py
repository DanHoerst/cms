from django.conf.urls.defaults import *
from django.contrib import admin, comments
from django.contrib.flatpages import urls
admin.autodiscover()

urlpatterns = patterns('',
    # Dependancies - TinyMCE
    url(r'^tiny_mce(?P<path>.*)$', 'django.views.static.serve', { 'document_root': '/home/dan/Downloads/tinymce/jscripts/tiny_mce' }),
    # Admin
    url(r'^admin/', include(admin.site.urls)),
    # Search
    url(r'^search/$', 'cms.search.views.search'),
    # Weblog categories include
    url(r'^weblog/categories/', include('cms.gambino.urls.categories')),
    # Weblog links include
    url(r'^weblog/links/', include('cms.gambino.urls.links')),
    # Weblog tags include
    url(r'^weblog/tags/', include('cms.gambino.urls.tags')),
    # Weblog entries include
    url(r'^weblog/', include('cms.gambino.urls.entries')),
    # Contact
    url(r'^contactus/$', 'cms.search.views.contactus'),
    # Comments
    url(r'^comments/', include('django.contrib.comments.urls')),
    # Catch All
    url(r'', include('django.contrib.flatpages.urls')),
)
