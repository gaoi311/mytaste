# -*- coding:utf-8 -*-

# author:   gaoi
# datetime: 3/29/20 1:58 PM
# software: PyCharm
from django.shortcuts import redirect


def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'username': user.username,
        'id': user.id
        # 'avator': user.avatar
    }


def login_required(fn):
    def inner(request, *args, **kwargs):
        if not request.COOKIES.get('is_login') == '1':
            next = request.path_info
            return redirect('/login/?next={}'.format(next))
        ret = fn(request, *args, **kwargs)
        return ret
    return inner
