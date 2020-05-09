# -*- coding:utf-8 -*-

# author:   gaoi
# datetime: 4/23/20 5:41 PM
# software: PyCharm

from rest_framework import serializers
from .models import *
from scene.serializers import CitySerializer


class HotelSummarySerializer(serializers.ModelSerializer):
    """
    酒店缩略信息
    """
    class Meta:
        model = Hotel
        fields = ['id', 'name', 'ename', 'main_photo', 'score', 'price', 'around', 'score_comment', 'grade']


class HotelDetailSerializer(serializers.ModelSerializer):
    """
    酒店详细信息
    """
    city = CitySerializer(read_only=True)

    class Meta:
        model = Hotel
        exclude = ['created_time', 'updated_time']


class HotelCommentSerializer(serializers.ModelSerializer):
    """
    酒店评论
    """
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
    """
    酒店房间
    """
    room_properties = serializers.SerializerMethodField(read_only=True)
    same_room_count = serializers.SerializerMethodField(read_only=True)

    def get_room_properties(self, obj):
        return {
            'type': obj.room_type.type,
            'area': obj.room_type.area,
            'has_tv': obj.room_type.has_tv,
            'has_phone': obj.room_type.has_phone,
            'has_toilet': obj.room_type.has_toilet
        }

    def get_same_room_count(self, obj):
        return HotelRoom.objects.filter(room_type=obj.room_type, hotel=obj.hotel).count()

    class Meta:
        model = HotelRoomType
        fields = ['id', 'room_properties', 'same_room_count']


class HotelRoomTypeSerializer(serializers.ModelSerializer):
    """
    酒店房间类型
    """
    count = serializers.SerializerMethodField(read_only=True)
    has_tv = serializers.SerializerMethodField(read_only=True)
    has_phone = serializers.SerializerMethodField(read_only=True)
    has_toilet = serializers.SerializerMethodField(read_only=True)

    def get_count(self, obj):
        return HotelRoom.objects.filter(status=0, hotel_id=obj.hotel.id, hotel_room_type_id=obj.id).count()

    def get_has_tv(self, obj):
        return obj.get_has_tv_display()

    def get_has_phone(self, obj):
        return obj.get_has_phone_display()

    def get_has_toilet(self, obj):
        return obj.get_has_toilet_display()

    class Meta:
        model = HotelRoomType
        fields = ['id', 'type', 'main_photo', 'price', 'area', 'has_tv', 'has_phone', 'has_toilet', 'count']


class HotelReservationSerializer(serializers.ModelSerializer):
    """
    酒店订单（用户足迹）
    """
    created_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)
    hotel_name = serializers.SerializerMethodField(read_only=True)
    hotel_photo = serializers.SerializerMethodField(read_only=True)

    def get_hotel_name(self, obj):
        return obj.hotel.name + '-' + obj.get_type_display()

    def get_hotel_photo(self, obj):
        return obj.hotel.main_photo.url

    class Meta:
        model = HotelReservation
        fields = ['id', 'hotel', 'created_time', 'hotel_name', 'hotel_photo']


class HotelSearchSerializer(serializers.ModelSerializer):
    """
    首页酒店模糊查询
    """
    class Meta:
        model = Hotel
        fields = ['id', 'name', 'around', 'address']
