import re

from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserModelSerializer
from .models import User


class UserAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


class PhoneAPIView(APIView):
    def get(self, request, phone):
        print(phone)
        if not re.match(r"^1[3-9]\d{9}$", phone):
            return Response(data={
                'message': "手机号码不正确"
            }, status=status.HTTP_400_BAD_REQUEST)
        # 验证手机号码是否已被注册
        if User.objects.filter(phone=phone):
            return Response(data={
                'message': "手机号已被注册"
            }, status=status.HTTP_400_BAD_REQUEST)
