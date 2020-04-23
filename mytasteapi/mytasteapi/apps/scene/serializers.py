#-*- coding:utf-8 -*-

# author:   gaoi
# datetime: 4/5/20 5:41 PM
# software: PyCharm

from rest_framework import serializers

from .models import Scene, City, Province

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'name', 'hot', 'summary']

class ProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = ['id', 'name']

class SceneSummarySerializer(serializers.ModelSerializer):
    city = CitySerializer()
    province = ProvinceSerializer()

    class Meta:
        model = Scene
        fields = ['id', 'name', 'hot', 'main_photo', 'grade', 'city', 'province']

class SceneSerializer(serializers.ModelSerializer):
    city = CitySerializer()
    province = ProvinceSerializer()

    class Meta:
        model = Scene
        exclude = ['created_time']