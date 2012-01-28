from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.contrib.flatpages import urls
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cms.views.home', name='home'),
    # url(r'^cms/', include('cms.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    
    url(r'^tiny_mce(?P<path>.*)$', 'django.views.static.serve', { 'document_root': '/home/dan/Downloads/tinymce/jscripts/tiny_mce' }),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^search/$', 'cms.search.views.search'),
    url(r'^weblog/$', 'gambino.views.entries_index'),
    url(r'^weblog/(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$', 'gambino.views.entry_detail'),
    url(r'', include(urls.urlpatterns)),
)
