from gambino.models import Category
from django.contrib import admin

class CategoryAdmin(admin.ModelAdmin):
    model = Category
    prepopulated_fields={'slug': ('title',)}

admin.site.register(Category, CategoryAdmin)
