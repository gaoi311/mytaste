# -*- coding:utf-8 -*-

# author:   gaoi
# datetime: 4/23/20 5:41 PM
# software: PyCharm

from rest_framework import serializers
from .models import Hotel, HotelComment
from scene.serializers import CitySerializer
from user.serializers import UserCommentSerializer


class HotelSerializer(serializers.ModelSerializer):
    city = CitySerializer(read_only=True)

    class Meta:
        model = Hotel
        exclude = ['created_time', 'updated_time']


class HotelCommentSerializer(serializers.ModelSerializer):
    user_info = serializers.SerializerMethodField(read_only=True)

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
