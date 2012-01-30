from django.conf.urls.defaults import *
from gambino.models import Category

# Category URLs
urlpatterns = patterns('',
    url(r'^$', 'django.views.generic.list_detail.object_list', { 'queryset': Category.objects.all() }),
    url(r'^(?P<slug>[-\w]+)/$', 'gambino.views.category_detail'),
)
