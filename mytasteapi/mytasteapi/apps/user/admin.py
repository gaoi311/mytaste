from django.contrib import admin
from .models import *


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'last_login', 'phone', 'is_staff', 'is_active')


class UserLovedSceneAdmin(admin.ModelAdmin):
    list_display = ('user', 'type', 'scene', 'created_time')

admin.site.register(User, UserAdmin)
admin.site.register(UserLovedScene, UserLovedSceneAdmin)
