import os
import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    GENDER_OPTION = (
        (1, "男"),
        (2, "女"),
        (3, "保密")
    )

    def user_directory_path(instance, filename):
        ext = filename.split('.')[-1]
        filename = '{}.{}'.format(uuid.uuid4().hex[:10], ext)
        return os.path.join(str(instance.id), "avatar", filename)

    phone = models.CharField(max_length=15, null=True, blank=True, unique=True, verbose_name="电话号码")
    wxchat = models.CharField(max_length=64, null=True, blank=True, unique=True, verbose_name="微信号")
    qq = models.CharField(max_length=15, null=True, blank=True, unique=True, verbose_name="QQ号")
    birth = models.DateField(null=True, blank=True, verbose_name="出生日期")
    gender = models.IntegerField(choices=GENDER_OPTION, default=3, verbose_name="性别")
    avatar = models.ImageField(upload_to=user_directory_path, default='0/avator/default.png', verbose_name="用户头像")
    county = models.CharField(max_length=100, blank=True, verbose_name="国家")
    province = models.CharField(max_length=100, blank=True, verbose_name="地区")
    city = models.CharField(max_length=100, blank=True, verbose_name="城市")
    address = models.CharField(max_length=100, blank=True, verbose_name="详细地址")
    updated_time = models.DateTimeField(auto_now=True, verbose_name="修改时间")

    class Meta:
        db_table = "mt_user"
        verbose_name = "用户"
        verbose_name_plural = verbose_name


class UserLovedScene(models.Model):
    TYPE_OPTION = (
        (1, "收藏"),
        (2, "去过"),
    )
    user = models.ForeignKey(to=User, verbose_name="用户", on_delete=models.CASCADE)
    scene = models.ForeignKey(to='scene.Scene', verbose_name="收藏景点", on_delete=models.CASCADE)
    type = models.IntegerField(choices=TYPE_OPTION, verbose_name="类型")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        db_table = "mt_user_scene"


class UserLovedHotel(models.Model):
    TYPE_OPTION = (
        (1, "收藏"),
        (2, "去过"),
    )
    user = models.ForeignKey(to=User, verbose_name="用户", on_delete=models.CASCADE)
    hotel = models.ForeignKey(to='hotel.Hotel', verbose_name="收藏酒店", on_delete=models.CASCADE)
    type = models.IntegerField(choices=TYPE_OPTION, verbose_name="类型")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        db_table = "mt_user_hotel"
