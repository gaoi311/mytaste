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


admin.site.register(Carousel, CarouselAdmin)
