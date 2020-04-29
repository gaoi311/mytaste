#-*- coding:utf-8 -*-

# author:   gaoi
# datetime: 3/27/20 9:20 PM
# software: PyCharm

from rest_framework import serializers

from .models import Carousel, NavigationBar

class CarouselModelSerializer(serializers.ModelSerializer):
    created_time = serializers.DateTimeField(format='%d %m/%Y', read_only=True)

    class Meta:
        model = Carousel
        fields = ['title', 'image_url', 'link', 'remark', 'created_time']


class HeaderNavigationModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = NavigationBar
        fields = ['title', 'link']


class FooterNavigationModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = NavigationBar
        fields = ['title', 'link']