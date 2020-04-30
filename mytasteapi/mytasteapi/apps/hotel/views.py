from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *
from .filters import *


class Pagination(PageNumberPagination):
    """
    分页
    """
    page_query_param = "page"
    page_size_query_param = "page_size"
    max_page_size = 100
    page_size = 1


class HotelsAPIView(APIView):
    """
    首页酒店缩略展示
    """

    def get(self, request):
        city = request.query_params.dict().get('city', "")
        hotel_queryset = Hotel.objects.filter(city=city).order_by('-score', 'price', '-comment_num')[:8]
        ser_obj = HotelSerializer(hotel_queryset, many=True)
        return Response(ser_obj.data)


class HotelAPIView(RetrieveAPIView):
    """
    单个景点详细展示
    """
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer


class HotelsListAPIView(APIView):
    """
    酒店列表筛选展示
    """

    def get(self, request, *args, **kwargs):
        city_id = kwargs.get('pk')

        hotel_around = request.query_params.dict().get('hotel_around')
        hotel_grade = request.query_params.dict().get('hotel_grade')
        hotel_order = request.query_params.dict().get('hotel_order')
        search_city = request.query_params.dict().get('search_city')

        if search_city:
            city_id = search_city
        hotels_queryset = Hotel.objects.filter(city_id=city_id).order_by('-score', 'price', '-grade')

        if hotel_around:
            hotels_queryset = hotels_queryset.filter(around__contains=hotel_around)
        if hotel_grade:
            hotels_queryset = hotels_queryset.filter(grade=hotel_grade)
        if hotel_order:
            hotels_queryset = hotels_queryset.order_by(hotel_order)

        page = Pagination()
        page_hotels = page.paginate_queryset(queryset=hotels_queryset, request=request, view=self)
        ser_obj = HotelSerializer(page_hotels, many=True)
        return page.get_paginated_response(ser_obj.data)


class HotelsSearchAPIView(ListAPIView):
    """
    首页酒店模糊搜索
    """
    serializer_class = HotelsSearchSerializer

    def get_queryset(self):
        query_string = self.request.query_params.dict().get('search', '')
        queryset = Hotel.objects.filter(
            Q(name__contains=query_string) | Q(around__contains=query_string) | Q(
                address__contains=query_string))

        return queryset


class HotelCommentAPIView(APIView):
    """
    酒店评论展示
    """

    def get(self, request, *args, **kwargs):
        hotel_id = kwargs.get('pk')
        page = Pagination()
        comments_queryset = HotelComment.objects.filter(hotel_id=hotel_id).order_by('-created_time')
        page_comments = page.paginate_queryset(queryset=comments_queryset, request=request, view=self)
        ser_obj = HotelCommentSerializer(page_comments, many=True)
        return page.get_paginated_response(ser_obj.data)


class HotelCommentCreateAPIView(CreateAPIView):
    """
    新增酒店评论
    """
    queryset = HotelComment.objects.all()
    serializer_class = HotelCommentSerializer


class HotelRoomAPIView(ListAPIView):
    """
    酒店房间展示
    """
    queryset = HotelRoom.objects.all()
    serializer_class = HotelRoomSerializer
    filter_backends = [DjangoFilterBackend, ]
    filter_fields = ['hotel']


class HotelRoomCheckAPIVIew(APIView):
    """
    酒店房间预订（修改）
    """

    def put(self, request, *args, **kwargs):
        room_id = kwargs.get('pk')
        room_obj = HotelRoom.objects.get(id=room_id)
        room_obj.room_count -= 1
        room_obj.save()

        hotel_id = request.data.get('hotel')
        user_id = request.data.get('user')
        HotelOrder.objects.create(hotel_id=hotel_id, user_id=user_id, room_id=room_id)

        return Response(HotelRoomSerializer(room_obj).data)


class HotelOrderAPIView(ListAPIView):
    """
    用户足迹展示（酒店记录）
    """
    queryset = HotelOrder.objects.all().order_by('-created_time')
    serializer_class = HotelOrderSerializer
    pagination_class = Pagination
    filter_backends = [DjangoFilterBackend, ]
    filter_fields = ['user']
