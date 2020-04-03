from django.contrib import admin

from .models import Carousel, NavigationBar


class CarouselAdmin(admin.ModelAdmin):
    list_display = ('title', 'remark', 'orders', 'is_show', 'is_deleted')
    fieldsets = (
        ['Main', {
            'fields': ('title', 'link', 'image_url', 'remark')
        }],
        ['Advance', {
            'fields': ('orders', 'is_show', 'is_deleted')
        }]
    )


class NavigationAdmin(admin.ModelAdmin):
    list_display = ('title', 'link', 'position', 'is_site', 'is_show', 'is_deleted')
    fieldsets = (
        ['Main', {
            'fields': ('title', 'link', 'position')
        }],
        ['Advance', {
            'fields': ('is_site', 'orders', 'is_show', 'is_deleted')
        }]
    )


admin.site.register(Carousel, CarouselAdmin)
admin.site.register(NavigationBar, NavigationAdmin)
