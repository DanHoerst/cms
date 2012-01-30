from django.shortcuts import get_object_or_404, render_to_response
from gambino.models import Category
from django.template import RequestContext

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render_to_response('gambino/category_detail.html',
                              { 'object_list': category.entry_set.all(),
                                'category': category })
