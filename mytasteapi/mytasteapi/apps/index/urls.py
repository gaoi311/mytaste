#-*- coding:utf-8 -*-

# author:   gaoi
# datetime: 3/27/20 9:20 PM
# software: PyCharm
from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('carousel/', views.CarouselListAPIView.as_view()),
    # url('nav/header/', views.HeaderNavigationListAPIView.as_view()),
    # url('nav/footer/', views.FooterNavigationListAPIView.as_view()),
]