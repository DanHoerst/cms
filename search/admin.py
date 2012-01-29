from search.models import SearchKeyword
from django.contrib import admin
from django.contrib.flatpages.models import FlatPage

# Sets up 3 inline keywords using SearchKeyWord model
class SearchKeywordInline(admin.StackedInline):
    model = SearchKeyword
    extra = 3

# Adds the 3 inline keywords to FlatPage section of admin
class FlatPageAdmin(admin.ModelAdmin):
    model = FlatPage
    inlines = [SearchKeywordInline]

# FlatPage app ships with it's own admin.py, so have to unregister and then register
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)
