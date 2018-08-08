from django.contrib import admin

from .models import Keyword, Category, Resource


class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    list_display = ('title', 'created_at')
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class ResourceInline(admin.StackedInline):
    model = Resource
    extra = 0


class KeywordAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at', 'visitor_counter')
    list_display = ('title', 'updated_at', 'is_public')
    fieldsets = [
        (None,               {'fields': ['title']}),
        (None,               {'fields': ['description']}),
        (None,               {'fields': ['categories']}),
        ('Admin Related', {'fields': ['slug', 'is_public']}),
        ('Non editable info', {'fields': ['visitor_counter', 'created_at', 'updated_at'],
                                'classes': ['collapse']})
    ]
    inlines = [ResourceInline]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Keyword, KeywordAdmin)
