# -*- coding:utf-8 -*-

# author:   gaoi
# datetime: 4/5/20 5:41 PM
# software: PyCharm

from rest_framework import serializers
from .models import Scene, City, Province, SceneComment


class CitySerializer(serializers.ModelSerializer):
    """
    城市信息
    """
    class Meta:
        model = City
        fields = ['id', 'name', 'hot', 'summary']


class ProvinceSerializer(serializers.ModelSerializer):
    """
    省份信息
    """
    class Meta:
        model = Province
        fields = ['id', 'name']


class SceneSummarySerializer(serializers.ModelSerializer):
    """
    景点缩略信息
    """
    # city = CitySerializer()
    # province = ProvinceSerializer()

    class Meta:
        model = Scene
        fields = ['id', 'name', 'ename', 'ticket', 'score', 'address', 'comment_num', 'hot', 'main_photo', 'grade']


class SceneDetailSerializer(serializers.ModelSerializer):
    """
    景点详细信息
    """
    city = CitySerializer()
    province = ProvinceSerializer()
    updated_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)

    class Meta:
        model = Scene
        exclude = ['created_time']


class SceneCommentSerializer(serializers.ModelSerializer):
    """
    景点评论信息
    """
    user_info = serializers.SerializerMethodField(read_only=True)
    created_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)

    def get_user_info(self, obj):
        return {
            "username": obj.user.phone,
            "avatar": obj.user.avatar.url
        }

    class Meta:
        model = SceneComment
        fields = "__all__"
        extra_kwargs = {
            "user": {
                "write_only": True
            },
            "scene": {
                "write_only": True
            }
        }


class SceneSearchSerializer(serializers.ModelSerializer):
    """
    首页景点模糊查询
    """
    class Meta:
        model = Scene
        fields = ['id', 'name', 'address']
