#-*- coding:utf-8 -*-

# author:   gaoi
# datetime: 3/29/20 9:20 AM
# software: PyCharm

from django.urls import path, re_path
from rest_framework_jwt.views import obtain_jwt_token
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    path('login/', obtain_jwt_token),
    path('register/', views.UserAPIView.as_view()),
    re_path(r'phone/(?P<phone>1[3-9]\d{9})/', views.PhoneAPIView.as_view())
]