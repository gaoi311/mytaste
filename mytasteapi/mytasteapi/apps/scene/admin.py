from django.contrib import admin

# Register your models here.
from .models import *

class SceneAdmin(admin.ModelAdmin):
    list_display = ('name', 'main_photo', 'address', 'grade', 'hot', 'ticket', 'updated_time')


admin.site.register(Scene, SceneAdmin)


class SceneCommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'scene', 'content','created_time')


admin.site.register(SceneComment, SceneCommentAdmin)