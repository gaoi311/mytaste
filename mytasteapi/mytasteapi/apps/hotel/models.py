import os
import uuid

from django.db import models

from scene.models import City
from smart_selects.db_fields import ChainedForeignKey
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


class HotelRoomType(models.Model):
    ROOM_TYPE = (
        (1, "标准间"),
        (2, "单人间"),
        (3, "双人间"),
        (4, "三人间"),
        (5, "大床房"),
        (6, "亲子间")
    )
    HAS_DEVICE = (
        (0, "无"),
        (1, "有")
    )

    def hotel_room_photo_path(instance, filename):
        ext = filename.split('.')[-1]
        filename = '{}.{}'.format(uuid.uuid4().hex[:10], ext)
        return os.path.join("hotelroom", filename)

    hotel = models.ForeignKey(to=Hotel, verbose_name="酒店", on_delete=models.CASCADE)
    type = models.IntegerField(choices=ROOM_TYPE, verbose_name="房型")
    main_photo = models.ImageField(upload_to=hotel_room_photo_path, default="0/avator/default.png", verbose_name="房型照片")
    price = models.IntegerField(verbose_name="房价")
    # count = models.IntegerField(verbose_name="房间数", default=0)
    area = models.IntegerField(verbose_name="面积")
    has_tv = models.IntegerField(choices=HAS_DEVICE, verbose_name="电视")
    has_phone = models.IntegerField(choices=HAS_DEVICE, verbose_name="电话")
    has_toilet = models.IntegerField(choices=HAS_DEVICE, verbose_name="独立卫生间")
    updated_time = models.DateTimeField(auto_now=True, verbose_name="修改时间")

    class Meta:
        db_table = "mt_hotel_room_type"
        verbose_name = "各酒店房间类型"
        verbose_name_plural = verbose_name
        unique_together = ('hotel', 'type')

    def __str__(self):
        return self.hotel.name + "-" + self.get_type_display()


class HotelRoom(models.Model):
    ROOM_STATUS = (
        (0, "空闲"),
        (1, "入住中"),
        (2, "已预订"),
        (3, "不可用")
    )
    hotel = models.ForeignKey(to=Hotel, on_delete=models.CASCADE, verbose_name="酒店")
    # room = ChainedForeignKey(
    #     to=HotelRoomType,
    #     chained_field="Hotel",
    #     chained_model_field="Hotel",
    #     show_all=False,
    #     auto_choose=True,
    #     sort=True
    # )
    hotel_room_type = models.ForeignKey(to=HotelRoomType, on_delete=models.CASCADE, verbose_name="房型")
    number = models.IntegerField(verbose_name="房间号码")
    status = models.IntegerField(choices=ROOM_STATUS, default=0, verbose_name="房间状态")
    class Meta:
        db_table = "mt_hotel_room"
        verbose_name = "酒店房间"
        verbose_name_plural = verbose_name
        unique_together = ('hotel', 'number')

    def __str__(self):
        return str(self.hotel) + str(self.number)


class HotelReservation(models.Model):
    ROOM_TYPE = (
        (1, "标准间"),
        (2, "单人间"),
        (3, "双人间"),
        (4, "三人间"),
        (5, "大床房"),
        (6, "亲子间")
    )
    user = models.ForeignKey(to=User, verbose_name="用户", on_delete=models.CASCADE)
    name = models.CharField(max_length=32, verbose_name="姓名")
    phone = models.CharField(max_length=15, verbose_name="电话")
    hotel = models.ForeignKey(to=Hotel, verbose_name="酒店", on_delete=models.CASCADE)
    type = models.IntegerField(choices=ROOM_TYPE, verbose_name="房间类型")
    people_number = models.IntegerField(default=1, verbose_name="入住人数")
    in_date = models.DateField(verbose_name="入住时间")
    out_date = models.DateField(verbose_name="离开时间")
    check_room_num = models.IntegerField(default=1, verbose_name="预订数量")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        db_table = "mt_hotel_reservation"
        verbose_name = "酒店预订"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.user) + str(self.hotel)

class HotelRoomOther(models.Model):
    hotel = models.ForeignKey(to=Hotel, on_delete=models.CASCADE, verbose_name="酒店")
    hotel_room_type = models.ForeignKey(to=HotelRoomType, on_delete=models.CASCADE, verbose_name="房型")
    count = models.IntegerField(verbose_name="空闲房间数")
    day = models.DateField(verbose_name="日期")
    class Meta:
        db_table = "mt_hotel_room_other"
        verbose_name = "酒店房间other"
        verbose_name_plural = verbose_name
        # unique_together = ('hotel', 'number')

    def __str__(self):
        return str(self.hotel) + str(self.hotel_room_type.get_type_display())