# -*- coding:utf-8 -*-

# author:   gaoi
# datetime: 4/23/20 9:20 PM
# software: PyCharm

from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path('hotel/(?P<pk>\d+)/', views.HotelAPIView.as_view()),
    re_path('hotels/(?P<pk>\d+)/', views.HotelsListAPIView.as_view()),
    re_path('hotel_comments/(?P<pk>\d+)/', views.HotelCommentAPIView.as_view()),
    path('hotel_comment/', views.HotelCommentCreateAPIView.as_view()),
    path('hotels/', views.HotelsAPIView.as_view()),
]
