from django.contrib import admin

# Register your models here.
from .models import *


class SceneAdmin(admin.ModelAdmin):
    list_display = ('name', 'main_photo', 'address', 'grade', 'hot', 'ticket', 'updated_time')
    search_fields = ('city__id', 'city__name')


class SceneCommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'scene', 'content', 'created_time')


class CityAdmin(admin.ModelAdmin):
    list_display = ('city_index', 'name', 'hot', 'province')


class ProvinceAdmin(admin.ModelAdmin):
    list_display = ('name', )

admin.site.register(Scene, SceneAdmin)
admin.site.register(SceneComment, SceneCommentAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Province, ProvinceAdmin)

