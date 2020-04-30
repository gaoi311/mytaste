from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'last_login', 'phone', 'is_staff', 'is_active')


admin.site.register(User, UserAdmin)
