from django.conf.urls.defaults import *
from gambino.models import Entry, Link
from tagging.models import Tag

# Tag URLs
urlpatterns = patterns('',
    url(r'^$', 'django.views.generic.list_detail.object_list', { 'queryset': Tag.objects.all() }, 'gambino_tag_list'),
    url(r'^entries/(?P<tag>[-\w]+)/$', 'tagging.views.tagged_object_list', { 'queryset_or_model': Entry.live.all(), 'template_name': 'gambino/entries_by_tag.html' }),
    url(r'^links/(?P<tag>[-\w]+)/$', 'tagging.views.tagged_object_list', { 'queryset_or_model': Link, 'template_name': 'gambino/links_by_tag.html' }),
)
