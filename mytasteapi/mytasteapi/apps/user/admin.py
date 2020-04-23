from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'last_login', 'birth')

admin.site.register(User, UserAdmin)