from django.shortcuts import render_to_response
from django.contrib.flatpages.models import FlatPage
from django.http import HttpResponseRedirect
from django.template import RequestContext

# If no query is entered, will bring you to blank search screen. Otherwise will pull results from keyword, and results from content and display in search.html
def search(request):
    query = request.GET.get('q', '')
    keyword_results = results = []
    if query:
        keyword_results = FlatPage.objects.filter(
searchkeyword__keyword__in=query.split()).distinct()
        if keyword_results.count() == 1:
            return HttpResponseRedirect(keyword_results[0].get_absolute_url())
        results = FlatPage.objects.filter(content__icontains=query)
    return render_to_response('search/search.html',
                              { 'query': query,
                                'keyword_results': keyword_results,
                                'results': results },
                              context_instance=RequestContext(request))

# Simple contactus.html display
def contactus(request):
    return render_to_response('search/contactus.html',
                              context_instance=RequestContext(request))
