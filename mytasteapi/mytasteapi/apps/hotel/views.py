import datetime

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


class HotelsSummaryAPIView(APIView):
    """
    首页酒店缩略展示
    """

    def get(self, request):
        city = request.query_params.dict().get('city', "")
        hotel_queryset = Hotel.objects.filter(city=city).order_by('-score', 'price', '-comment_num')[:8]
        ser_obj = HotelSummarySerializer(hotel_queryset, many=True)
        return Response(ser_obj.data)


class HotelDetailAPIView(RetrieveAPIView):
    """
    单个景点详细展示
    """
    queryset = Hotel.objects.all()
    serializer_class = HotelDetailSerializer


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
        ser_obj = HotelSummarySerializer(page_hotels, many=True)
        return page.get_paginated_response(ser_obj.data)


class HotelsSearchAPIView(ListAPIView):
    """
    首页酒店模糊搜索
    """
    serializer_class = HotelSearchSerializer

    def get_queryset(self):
        query_string = self.request.query_params.dict().get('search', '')
        queryset = Hotel.objects.filter(
            Q(name__contains=query_string) | Q(around__contains=query_string) | Q(
                address__contains=query_string))

        return queryset


class HotelCommentsAPIView(APIView):
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


# class HotelRoomsAPIView(ListAPIView):
#     """
#     酒店房间类型展示
#     """
#     queryset = HotelRoomType.objects.all()
#     serializer_class = HotelRoomTypeSerializer
#     filter_backends = [DjangoFilterBackend, ]
#     filter_fields = ['hotel']


# class HotelRoomCheckAPIVIew(APIView):
#     """
#     酒店房间预订（修改）
#     """
#     def post(self, request, *args, **kwargs):
#         user = int(request.data.get('user'))
#         in_date = request.data.get('in_date')
#         out_date = request.data.get('out_date')
#         name = request.data.get('name')
#         phone = request.data.get('phone')
#         hotel = int(request.data.get('hotel'))
#         type = int(request.data.get('type'))
#         check_room_num = int(request.data.get('check_room_num'))
#
#
#         blank_rooms = HotelRoom.objects.filter(hotel=hotel, status=0, hotel_room_type__type=type)
#         if blank_rooms.count() < check_room_num:
#             return Response(data={'status': -1, 'message': "没有足够的房间了"})
#
#         blank_rooms = blank_rooms.order_by('number')[:check_room_num]
#         for blank_room in blank_rooms:
#             blank_room.status = 2
#             blank_room.save()
#
#         HotelReservation.objects.create(in_date=in_date, out_date=out_date, hotel_id=hotel, type=type, user_id=user, check_room_num=check_room_num, phone=phone, name=name).save()
#         return Response(data={'status': 1, 'message': "预订成功"})


class HotelReservationAPIView(ListAPIView):
    """
    用户足迹展示（酒店记录）
    """
    queryset = HotelReservation.objects.all().order_by('-created_time')
    serializer_class = HotelReservationSerializer
    pagination_class = Pagination
    filter_backends = [DjangoFilterBackend, ]
    filter_fields = ['user']


class HotelRoomsAPIView(APIView):
    """
    酒店房间类型展示
    """

    def get(self, request):
        hotel = request.query_params.dict().get('hotel')
        day = request.query_params.dict().get('day')

        # if day is not None:
        #     day = day[0]

        rooms_queryset = HotelRoomOther.objects.filter(hotel_id=hotel, day=day)
        ser_obj = HotelRoomOtherSerializer(rooms_queryset, many=True)
        return Response(ser_obj.data)


class HotelRoomCheckAPIVIew(APIView):
    """
    酒店房间预订（修改）
    """

    def post(self, request, *args, **kwargs):
        user = int(request.data.get('user'))
        in_date = request.data.get('in_date')
        out_date = request.data.get('out_date')
        name = request.data.get('name')
        phone = request.data.get('phone')
        hotel = int(request.data.get('hotel'))
        type = int(request.data.get('type'))
        check_room_num = int(request.data.get('check_room_num'))

        blank_rooms = HotelRoomOther.objects.filter(hotel=hotel, hotel_room_type__type=type)

        pass_date = in_date
        stop_date = out_date
        # 判断每天的房间数是否都够用
        while pass_date != stop_date:
            every_day_blank_rooms = blank_rooms.filter(day=pass_date)
            if not every_day_blank_rooms:
                return Response(data={'status': -2, 'message': "只能预订今后五天内的房间哦！"})
            if every_day_blank_rooms[0].count < check_room_num:
                return Response(data={'status': -3, 'message': pass_date + "房间不够用哦！"})
            pass_date = datetime.datetime.strftime(
                datetime.datetime.strptime(pass_date, "%Y-%m-%d") + datetime.timedelta(days=1), '%Y-%m-%d')

        pass_date = in_date
        stop_date = out_date
        # 每天都够用的情况下，减去所需房间数
        while pass_date != stop_date:
            blank_room = blank_rooms.get(day=pass_date)
            blank_room.count -= check_room_num
            blank_room.save()
            pass_date = datetime.datetime.strftime(
                datetime.datetime.strptime(pass_date, "%Y-%m-%d") + datetime.timedelta(days=1), '%Y-%m-%d')


        HotelReservation.objects.create(in_date=in_date, out_date=out_date, hotel_id=hotel, type=type, user_id=user,
                                        check_room_num=check_room_num, phone=phone, name=name).save()
        return Response(data={'status': 1, 'message': "预订成功"})
