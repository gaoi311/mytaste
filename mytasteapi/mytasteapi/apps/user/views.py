import re

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserModelSerializer, UserLovedHotelSerializer, UserLovedSceneSerializer, UserInfoSerializer
from .models import User, UserLovedScene, UserLovedHotel


class Pagination(PageNumberPagination):
    page_query_param = "page"
    page_size_query_param = "page_size"
    max_page_size = 100
    page_size = 4


class UserAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


class PhoneAPIView(APIView):
    def get(self, request, phone):
        if not re.match(r"^1[3-9]\d{9}$", phone):
            return Response(data={
                'message': "手机号码不正确"
            }, status=status.HTTP_400_BAD_REQUEST)
        # 验证手机号码是否已被注册
        if User.objects.filter(phone=phone):
            return Response(data={
                'message': "手机号已被注册"
            }, status=status.HTTP_400_BAD_REQUEST)


class UserLovedSceneAPIView(ListAPIView):
    queryset = UserLovedScene.objects.all().order_by('-created_time')
    serializer_class = UserLovedSceneSerializer
    pagination_class = Pagination
    filter_backends = [DjangoFilterBackend, ]
    filter_fields = ['type', 'user']


class UserLovedHotelAPIView(ListAPIView):
    queryset = UserLovedHotel.objects.all().order_by('-created_time')
    serializer_class = UserLovedHotelSerializer
    pagination_class = Pagination
    filter_backends = [DjangoFilterBackend, ]
    filter_fields = ['type', 'user']


class UserSceneLovedCreateAPIView(CreateAPIView):
    queryset = UserLovedScene.objects.all()
    serializer_class = UserLovedSceneSerializer


class UserHotelLovedCreateAPIView(CreateAPIView):
    queryset = UserLovedHotel.objects.all()
    serializer_class = UserLovedHotelSerializer


class UserInfoAPIView(RetrieveAPIView, UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserInfoSerializer