import re
import random

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.pagination import PageNumberPagination
from django_redis import get_redis_connection
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *
from .models import *
from mytasteapi.settings import constants
from mytasteapi.libs.yuntongxun.sms import CCP


class Pagination(PageNumberPagination):
    """分页"""
    page_query_param = "page"
    page_size_query_param = "page_size"
    max_page_size = 100
    page_size = 4


class UserAPIView(CreateAPIView):
    """
    新增用户
    """
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


class UserLovedSceneAPIView(ListAPIView):
    """
    用户收藏、去过的景点
    """
    queryset = UserLovedScene.objects.all().order_by('-created_time')
    serializer_class = UserLovedSceneSerializer
    pagination_class = Pagination
    filter_backends = [DjangoFilterBackend, ]
    filter_fields = ['type', 'user']


# class UserLovedHotelAPIView(ListAPIView):
#     queryset = UserLovedHotel.objects.all().order_by('-created_time')
#     serializer_class = UserLovedHotelSerializer
#     pagination_class = Pagination
#     filter_backends = [DjangoFilterBackend, ]
#     filter_fields = ['type', 'user']


class UserSceneLovedCreateAPIView(CreateAPIView):
    """
    新增用户收藏、去过景点
    """
    queryset = UserLovedScene.objects.all()
    serializer_class = UserLovedSceneSerializer


# class UserHotelLovedCreateAPIView(CreateAPIView):
#     queryset = UserLovedHotel.objects.all()
#     serializer_class = UserLovedHotelSerializer


class UserInfoAPIView(RetrieveAPIView, UpdateAPIView):
    """
    用户信息展示、修改
    """
    queryset = User.objects.all()
    serializer_class = UserInfoSerializer


class SmsAPIView(APIView):
    def get(self, request, phone):
        """"发送验证码"""
        if User.objects.filter(phone=phone):
            return Response({'status': -1, 'message': '手机号已被注册！'})
        redis_conn = get_redis_connection("sms_code")
        ret = redis_conn.get("phone_%s" % phone)
        if ret is not None:
            return Response({'status': 101, 'message': "验证码已发送，请耐心等待！"})

        sms_code = "%06d" % random.randint(1, 999999)
        print(sms_code)
        # 创建管道对象
        pipe = redis_conn.pipeline()
        # 执行事务
        pipe.multi()

        pipe.setex("sms_%s" % phone, constants.SMS_EXPIRE_TIME, sms_code)
        pipe.setex("phone_%s" % phone, constants.SMS_INTERVAL_TIME, '_')

        # 执行事物
        pipe.execute()
        try:
            print(1)
            ccp = CCP()
            print(2)
            ret = ccp.send_template_sms(phone, [sms_code, constants.SMS_EXPIRE_TIME // 60], constants.SMS_TEMPLATE_ID)
            print(ret)
        except:
            return Response({'status': -2, 'message': "发送短信失败！"})

        return Response({'status': 1, 'message': "发送短信成功！"})