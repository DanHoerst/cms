from gambino.models import Category, Entry, Link
from django.contrib import admin

# Category Admin from Category - prepop slug from title
class CategoryAdmin(admin.ModelAdmin):
    model = Category
    prepopulated_fields={'slug': ('title',)}

# Entry Admin from Entry - prepop slug from title
class EntryAdmin(admin.ModelAdmin):
    model = Entry
    prepopulated_fields={'slug': ('title',)}

# Link Admin from Link - prepop slug from title
class LinkAdmin(admin.ModelAdmin):
    model = Link
    prepopulated_fields={'slug': ('title',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Entry, EntryAdmin)
admin.site.register(Link, LinkAdmin)
