from django.contrib import admin

# Register your models here.
from .models import *


class HotelAdmin(admin.ModelAdmin):
    list_display = ('name', 'main_photo', 'grade', 'price', 'updated_time')


class HotelCommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'hotel', 'content', 'created_time')


class HotelRoomTypeAdmin(admin.ModelAdmin):
    list_display = ('hotel', 'type', 'price', 'has_tv', 'has_phone', 'has_toilet', 'updated_time')


class HotelRoomAdmin(admin.ModelAdmin):
    list_display = ('hotel', 'hotel_room_type', 'number', 'status')


class HotelReservationAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'name', 'phone', 'hotel', 'type', 'check_room_num', 'in_date', 'out_date')


class HotelRoomOtherAdmin(admin.ModelAdmin):
    list_display = ('hotel', 'hotel_room_type', 'day', 'count')


admin.site.register(Hotel, HotelAdmin)
admin.site.register(HotelComment, HotelCommentAdmin)
admin.site.register(HotelRoomType, HotelRoomTypeAdmin)
admin.site.register(HotelRoom, HotelRoomAdmin)
admin.site.register(HotelReservation, HotelReservationAdmin)
admin.site.register(HotelRoomOther, HotelRoomOtherAdmin)