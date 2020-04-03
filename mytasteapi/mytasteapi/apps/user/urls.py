#-*- coding:utf-8 -*-

# author:   gaoi
# datetime: 3/29/20 9:20 AM
# software: PyCharm

from django.conf.urls import url
from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from django.views.decorators.csrf import csrf_exempt

from .views import LoginView, RegisterView

urlpatterns = [
    # path(r'login/', obtain_jwt_token),
    path('login/', csrf_exempt(LoginView.as_view())),
    path('register/', csrf_exempt(RegisterView.as_view())),
]