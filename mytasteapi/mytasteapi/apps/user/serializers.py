# -*- coding:utf-8 -*-

# author:   gaoi
# datetime: 4/5/20 11:37 AM
# software: PyCharm
import re

from django.contrib.auth.hashers import make_password
from rest_framework.validators import UniqueValidator
from rest_framework_jwt import serializers as jwt_serializers
from rest_framework import serializers
from .models import User, UserLovedHotel, UserLovedScene


class UserModelSerializer(serializers.ModelSerializer):
    # sms_code = serializers.CharField(min_length=4, max_length=6, required=True, write_only=True, help_text="短信验证码")
    token = serializers.CharField(max_length=1024, read_only=True, help_text="token认证字符串")
    #########################################################
    #                                                       #
    #特别注意，在进行唯一性验证时，此处就开始，不会等到钩子函数！！#
    #                                                       #
    #########################################################
    phone = serializers.CharField(max_length=15, validators=[UniqueValidator(queryset=User.objects.all(), message="手机号已被注册！")])

    class Meta:
        model = User
        fields = ['id', 'phone', 'password', 'username', 'token']
        # fields = ['id', 'phone', 'password', 'username', 'token', 'sms_code']

        extra_kwargs = {
            'phone': {
                'write_only': True
            },
            'password': {
                'write_only': True
            },
            'id': {
                'read_only': True
            },
            'username': {
                'read_only': True
            }
        }

    def validate(self, attrs):
        phone = attrs.get('phone')
        # sms_code = attrs.get('sms_code')
        password = attrs.get('password')
        # 验证手机格式
        if not re.match(r"^1[3-9]\d{9}$", phone):
            raise serializers.ValidationError("手机号码格式有误！")
        # todo 验证短信验证码是否正确
        return attrs

    def create(self, validated_data):
        # 移除sms_code
        # validated_data.pop("sms_code")
        # 密码加密
        raw_password = validated_data.get('password')
        hash_password = make_password(password=raw_password)
        # 使用手机号作为默认用户名
        username = validated_data.get('phone')
        user = User.objects.create(phone=username, username=username, password=hash_password)
        # 注册及登录，生成token
        payload = jwt_serializers.jwt_payload_handler(user)
        user.token = jwt_serializers.jwt_encode_handler(payload)
        return user


class UserCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'avatar']


class UserLovedHotelSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only=True)
    main_photo = serializers.SerializerMethodField(read_only=True)
    created_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)

    def get_main_photo(self, obj):
        return obj.hotel.main_photo.url

    def get_name(self, obj):
        return obj.hotel.name

    class Meta:
        model = UserLovedHotel
        fields = "__all__"


class UserLovedSceneSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only=True)
    main_photo = serializers.SerializerMethodField(read_only=True)
    created_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)

    def get_main_photo(self, obj):
        return obj.scene.main_photo.url

    def get_name(self, obj):
        return obj.scene.name

    class Meta:
        model = UserLovedScene
        fields = "__all__"


class UserInfoSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=150,
                                  validators=[UniqueValidator(queryset=User.objects.all(), message="用户名已经有人用过了哦！")])

    email = serializers.CharField(max_length=254,
                                  validators=[UniqueValidator(queryset=User.objects.all(), message="邮箱已经有人用过了哦！")])
    class Meta:
        model = User
        fields = ['username', 'email', 'birth', 'gender', 'address']