# -*- coding:utf-8 -*-

# author:   gaoi
# datetime: 4/3/20 4:49 PM
# software: PyCharm
from django.contrib.auth.backends import ModelBackend

from user.models import User


class MutliLogin(ModelBackend):
    """
    多条件登录
    """
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(username=username)
        except:
            try:
                user = User.objects.get(phone=username)
            except:
                try:
                    user = User.objects.get(email=username)
                except:
                    return None
        # 判断密码
        if user.check_password(password):
            return user
        else:
            return None


def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'username': user.username,
        'id': user.id,
        'avatar': user.avatar.url
    }