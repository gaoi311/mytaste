# -*- coding:utf-8 -*-

# author:   gaoi
# datetime: 3/28/20 2:20 PM
# software: PyCharm
from django.db import models


class Base(models.Model):
    """
    可复用的属性
    """
    orders = models.IntegerField(default=1, verbose_name="排序")
    is_show = models.BooleanField(default=True, verbose_name="是否显示")
    is_deleted = models.BooleanField(default=False, verbose_name="是否删除")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_time = models.DateTimeField(auto_now=True, verbose_name="修改时间")

    class Meta:
        # 设置抽象类，作为基类不会被创建表
        abstract = True