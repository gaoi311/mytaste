import json

from django.http import JsonResponse
from django.views import View
from django.contrib.auth.hashers import make_password, check_password

from .models import User
from mytasteapi.settings.constants import *


class LoginView(View):
    def post(self, request, *args, **kwargs):
        body = json.loads(request.body)
        phone = body.get('phone')
        password = body.get('password')

        # 使用django内置方法加密，盐为密码
        password_secret = make_password(password=password, salt=password)

        user = User.objects.filter(phone=phone, password=password_secret).first()

        if user:
            response = JsonResponse(data={
                'username': user.username or user.phone or user.email,
                'id': user.id
            })
            response.set_cookie('logined', '1', max_age=COOKIE_MAX_AGE)  # cookie默认设置一周
            return response


class RegisterView(View):
    def post(self, request, *args, **kwargs):
        body = json.loads(request.body)
        phone = body.get('phone')  # 手机或邮箱，默认为手机
        password = body.get('password')

        user = User.objects.filter(phone=phone)
        if user or (not phone) or (not password):
            return JsonResponse(data={
                'ok': 0
            })
        password_secret = make_password(password=password, salt=password)

        user = User.objects.create(phone=phone, password=password_secret)
        response = JsonResponse(data={
            'ok': 1,
            'username': user.username or user.phone or user.email,
            'id': user.id
        })
        response.set_cookie('logined', '1', max_age=COOKIE_MAX_AGE)
        return response
