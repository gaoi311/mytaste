from django.contrib import admin

# Register your models here.
from .models import *

class HotelAdmin(admin.ModelAdmin):
    list_display = ('name', 'main_photo', 'grade', 'price', 'updated_time')


class HotelCommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'hotel', 'content','created_time')


class HotelRoomAdmin(admin.ModelAdmin):
    list_display = ('hotel', 'room_type', 'room_count', 'room_price', 'updated_time')


class HotelOrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'hotel', 'room', 'created_time')

admin.site.register(Hotel, HotelAdmin)
admin.site.register(HotelComment, HotelCommentAdmin)
admin.site.register(HotelRoom, HotelRoomAdmin)
admin.site.register(HotelOrder, HotelOrderAdmin)