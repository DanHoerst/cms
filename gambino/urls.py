from django.conf.urls.defaults import *
from gambino.models import Entry

# define entry_info_dict used for generic view
entry_info_dict = {
    'queryset': Entry.objects.all(),
    'date_field': 'pub_date',
}

urlpatterns = patterns('django.views.generic.date_based',
    # Weblog index - Generic View
    url(r'^$', 'archive_index', entry_info_dict, 'gambino_entry_archive_index'),
    # Archive year - Generic View
    url(r'^(?P<year>\d{4})/$', 'archive_year', entry_info_dict, 'gambino_entry_archive_year'),
    # Archive month - Generic View
    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/$', 'archive_month', entry_info_dict, 'gambino_entry_archive_month'),
    # Archive day - Generic View
    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/$', 'archive_day', entry_info_dict, 'gambino_entry_archive_day'),
    # Weblog detail - Generic View
    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$', 'object_detail', entry_info_dict, 'gambino_entry_detail'),
)
