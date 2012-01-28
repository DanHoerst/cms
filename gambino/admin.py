from gambino.models import Category, Entry
from django.contrib import admin

class CategoryAdmin(admin.ModelAdmin):
    model = Category
    prepopulated_fields={'slug': ('title',)}

class EntryAdmin(admin.ModelAdmin):
    model = Entry
    prepopulated_fields={'slug': ('title',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Entry, EntryAdmin)
