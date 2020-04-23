# -*- coding:utf-8 -*-

# author:   gaoi
# datetime: 4/5/20 11:37 AM
# software: PyCharm
import re

from django.contrib.auth.hashers import make_password
from rest_framework_jwt import serializers as jwt_serializers
from rest_framework import serializers
from .models import User

class UserModelSerializer(serializers.ModelSerializer):
    sms_code = serializers.CharField(min_length=4, max_length=6, required=True, write_only=True, help_text="短信验证码")
    token = serializers.CharField(max_length=1024, read_only=True, help_text="token认证字符串")

    class Meta:
        model = User
        fields = ['id', 'phone', 'password', 'username', 'token', 'sms_code']
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
        sms_code = attrs.get('sms_code')
        password = attrs.get('password')
        # 验证手机格式
        if not re.match(r"^1[3-9]\d{9}$", phone):
            raise serializers.ValidationError("手机号码格式有误！")
        # 验证手机号码是否已被注册
        if User.objects.filter(phone=phone):
            raise serializers.ValidationError("手机号已被注册！")
        # todo 验证短信验证码是否正确
        return attrs

    def create(self, validated_data):
        # 移除sms_code
        validated_data.pop("sms_code")
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
