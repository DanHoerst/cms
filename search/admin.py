from search.models import SearchKeyword
from django.contrib import admin
from django.contrib.flatpages.models import FlatPage

class SearchKeywordInline(admin.StackedInline):
    model = SearchKeyword
    extra = 3

class FlatPageAdmin(admin.ModelAdmin):
    model = FlatPage
    inlines = [SearchKeywordInline]

admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)
