# -*- coding:utf-8 -*-

# author:   gaoi
# datetime: 3/29/20 9:20 AM
# software: PyCharm

from django.urls import path, re_path
from rest_framework_jwt.views import obtain_jwt_token
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    re_path('phone/(?P<phone>1[3-9]\d{9})/', views.PhoneAPIView.as_view()),
    re_path('user/info/(?P<pk>\d+)/', views.UserInfoAPIView.as_view()),
    path('login/', obtain_jwt_token),
    path('register/', views.UserAPIView.as_view()),
    path('user/loved_scene/', views.UserLovedSceneAPIView.as_view()),
    # path('user/loved_hotel/', views.UserLovedHotelAPIView.as_view()),
    path('user/new_loved_scene/', views.UserSceneLovedCreateAPIView.as_view()),
    # path('user/new_loved_hotel/', views.UserHotelLovedCreateAPIView.as_view())
]
