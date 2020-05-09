# -*- coding:utf-8 -*-

# author:   gaoi
# datetime: 4/23/20 9:20 PM
# software: PyCharm

from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path('hotel/(?P<pk>\d+)/', views.HotelDetailAPIView.as_view()),
    re_path('hotelslist/(?P<pk>\d+)/', views.HotelsListAPIView.as_view()),
    re_path('hotel_comments/(?P<pk>\d+)/', views.HotelCommentsAPIView.as_view()),
    re_path('room/', views.HotelRoomCheckAPIVIew.as_view()),
    path('hotel_comment/', views.HotelCommentCreateAPIView.as_view()),
    path('hotels/', views.HotelsSummaryAPIView.as_view()),
    path('rooms/', views.HotelRoomsAPIView.as_view()),
    path('went_hotels/', views.HotelReservationAPIView.as_view()),
    path('fuzzy_hotels/', views.HotelsSearchAPIView.as_view()),
]
