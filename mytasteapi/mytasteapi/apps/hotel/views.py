from django.shortcuts import render

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django_filters import rest_framework
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Hotel, HotelComment
from .serializers import HotelSerializer, HotelCommentSerializer


class Pagination(PageNumberPagination):
    page_query_param = "page"
    page_size_query_param = "page_size"
    max_page_size = 100
    page_size = 1


class HotelsAPIView(APIView):
    def get(self, request):
        city = request.query_params.dict().get('city', "")
        hotel_queryset = Hotel.objects.filter(city=city).order_by('-score', 'price', '-comment_num')[:8]
        ser_obj = HotelSerializer(hotel_queryset, many=True)
        return Response(ser_obj.data)


class HotelAPIView(RetrieveAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer


class HotelsListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        city_id = kwargs.get('pk', )
        page = Pagination()
        hotels_queryset = Hotel.objects.filter(city_id=city_id).order_by('-score', 'price', '-grade')
        page_hotels = page.paginate_queryset(queryset=hotels_queryset, request=request, view=self)
        ser_obj = HotelSerializer(page_hotels, many=True)
        return page.get_paginated_response(ser_obj.data)


class HotelCommentAPIView(APIView):
    def get(self, request, *args, **kwargs):
        hotel_id = kwargs.get('pk')
        page = Pagination()
        comments_queryset = HotelComment.objects.filter(hotel_id=hotel_id).order_by('-created_time')
        page_comments = page.paginate_queryset(queryset=comments_queryset, request=request, view=self)
        ser_obj = HotelCommentSerializer(page_comments, many=True)
        return page.get_paginated_response(ser_obj.data)


class HotelCommentCreateAPIView(CreateAPIView):
    queryset = HotelComment
    serializer_class = HotelCommentSerializer