from django.conf.urls.defaults import *
from gambino.models import Link

# define link_info_dict used for generic view
link_info_dict = {
    'queryset': Link.objects.all(),
    'date_field': 'pub_date',
}

# Generic Views URL Patterns
urlpatterns = patterns('django.views.generic.date_based',
    # Links Archive Index
    url(r'^$', 'archive_index', link_info_dict, 'gambino_link_archive_index'),
    # Links Archive Year
    url(r'^(?P<year>\d{4})/$', 'archive_year', link_info_dict, 'gambino_link_archive_year'),
    # Links Archive Month
    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/$', 'archive_month', link_info_dict, 'gambino_link_archive_month'),
    # Links Archive Day
    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/$', 'archive_day', link_info_dict, 'gambino_link_archive_day'),
    # Links Detail
    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$', 'object_detail', link_info_dict, 'gambino_link_detail'), 
)
