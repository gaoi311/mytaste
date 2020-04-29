# -*- coding:utf-8 -*-

# author:   gaoi
# datetime: 4/23/20 5:41 PM
# software: PyCharm

from rest_framework import serializers
from .models import *
from scene.serializers import CitySerializer
from user.serializers import UserCommentSerializer


class HotelSerializer(serializers.ModelSerializer):
    city = CitySerializer(read_only=True)

    class Meta:
        model = Hotel
        exclude = ['created_time', 'updated_time']


class HotelCommentSerializer(serializers.ModelSerializer):
    user_info = serializers.SerializerMethodField(read_only=True)
    created_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)

    def get_user_info(self, obj):
        return {
            "username": obj.user.phone,
            "avatar": obj.user.avatar.url
        }
    class Meta:
        model = HotelComment
        fields = "__all__"
        extra_kwargs = {
            "user": {
                "write_only": True
            },
            "hotel": {
                "write_only": True
            }
        }

class HotelRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelRoom
        fields = ['id', 'room_type', 'room_count', 'room_price']


class HotelOrderSerializer(serializers.ModelSerializer):
    created_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)
    hotel_name = serializers.SerializerMethodField(read_only=True)
    hotel_photo = serializers.SerializerMethodField(read_only=True)

    def get_hotel_name(self, obj):
        return obj.hotel.name + '-' + obj.room.room_type

    def get_hotel_photo(self, obj):
        return obj.hotel.main_photo.url

    class Meta:
        model = HotelOrder
        fields = ['id', 'hotel', 'created_time', 'hotel_name', 'hotel_photo']

class HotelsSearchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hotel
        fields = ['id', 'name', 'around', 'address']