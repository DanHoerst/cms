from django.shortcuts import get_object_or_404, render_to_response
from gambino.models import Entry
from django.template import RequestContext

# Displays all entries. Using context_instance for CSS inclusion.
def entries_index(request):
    return render_to_response('gambino/entry_index.html',
                              { 'entry_list': Entry.objects.all() },
                              context_instance=RequestContext(request))

# Displays specific entry from uls.py (/weblog/(4 digit year)/(3 letter month)/(2 digit day)/(slug). Using context_instance for CSS inclusion.
def entry_detail(request, year, month, day, slug):
    import datetime, time
    date_stamp = time.strptime(year+month+day, "%Y%b%d")
    pub_date = datetime.date(*date_stamp[:3])
    entry = get_object_or_404(Entry, pub_date__year=pub_date.year,
                                     pub_date__month=pub_date.month,
                                     pub_date__day=pub_date.day, 
                                     slug=slug)
    return render_to_response('gambino/entry_detail.html', { 'entry': entry },
                              context_instance=RequestContext(request))
