from django.db import models

from scene.models import City
from user.models import User


class Hotel(models.Model):
    GRADE_OPTION = (
        (1, "无"),
        (2, "一星级"),
        (3, "二星级"),
        (4, "三星级"),
        (5, "四星级"),
        (6, "五星级")
    )
    name = models.CharField(max_length=255, verbose_name="酒店名称")
    ename = models.CharField(max_length=255, blank=True, verbose_name="英文名称")
    city = models.ForeignKey(to=City, on_delete=models.CASCADE, verbose_name="所在城市")
    country = models.CharField(max_length=255, default="中国", verbose_name="所在国家")
    address = models.CharField(max_length=1024, blank=True, verbose_name="地址")
    main_photo = models.ImageField(upload_to="hotel", blank=True, null=True, verbose_name="主展示图片")
    score = models.CharField(max_length=10, default="暂无评分", verbose_name="评分")
    comment_num = models.IntegerField(default=0, verbose_name="评论数")
    grade = models.IntegerField(choices=GRADE_OPTION, default=1, verbose_name="星级")
    summary = models.TextField(blank=True, verbose_name="景点介绍")
    phone = models.CharField(max_length=1024, blank=True, verbose_name="联系电话")
    price = models.CharField(max_length=8, default="暂无", verbose_name="价格")
    score_comment = models.CharField(max_length=255, blank=True, verbose_name="评分评价")
    traffic = models.CharField(max_length=1024, blank=True, verbose_name="交通")
    around = models.CharField(max_length=255, blank=True, verbose_name="周边")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_time = models.DateTimeField(auto_now=True, verbose_name="修改时间")

    class Meta:
        db_table = "mt_hotel"
        verbose_name = "酒店"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class HotelComment(models.Model):
    content = models.CharField(max_length=1024, verbose_name="评论内容")
    score = models.SmallIntegerField(verbose_name="评分")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="发表时间")
    user = models.ForeignKey(to=User, verbose_name="用户", on_delete=models.CASCADE)
    hotel = models.ForeignKey(to=Hotel, verbose_name="酒店", on_delete=models.CASCADE)

    class Meta:
        db_table = "mt_hotel_comment"
        verbose_name = "酒店评论"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.user) + str(self.hotel)