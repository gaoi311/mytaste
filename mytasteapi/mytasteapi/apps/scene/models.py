from django.db import models

from user.models import User


class Province(models.Model):
    name = models.CharField(max_length=50, verbose_name="省份")

    class Meta:
        db_table = 'mt_province'
        verbose_name = "省份"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class City(models.Model):
    city_index = models.IntegerField(verbose_name="省属市索引")
    province = models.ForeignKey(to=Province, on_delete=models.CASCADE, verbose_name="所在省")
    name = models.CharField(max_length=100, verbose_name="名称")
    hot = models.IntegerField(default=1000, verbose_name="热度")
    summary = models.CharField(max_length=1024, default="", verbose_name="景点概括")

    class Meta:
        db_table = 'mt_city'
        verbose_name = "地级市"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Scene(models.Model):
    TYPE_OPTION = (
        (1, "其他"),
        (2, "自然"),
        (3, "文化"),
        (4, "历史"),
        (5, "建筑"),
        (6, "公园"),
        (7, "休闲")
    )
    GRADE_OPTION = (
        (1, "无"),
        (2, "A级"),
        (3, "AA级"),
        (4, "AAA级"),
        (5, "AAAA级"),
        (6, "AAAAA级")
    )
    name = models.CharField(max_length=255, verbose_name="景点名称")
    ename = models.CharField(max_length=255, blank=True, verbose_name="英文名称")
    city = models.ForeignKey(to=City, on_delete=models.CASCADE, verbose_name="所在城市")
    province = models.ForeignKey(to=Province, on_delete=models.CASCADE, verbose_name="所在省")
    country = models.CharField(max_length=255, default="中国", verbose_name="所在国家")
    address = models.CharField(max_length=1024, blank=True, verbose_name="地址")
    hot = models.IntegerField(default=0, verbose_name="热度（点击量）")
    main_photo = models.ImageField(upload_to="scene", blank=True, null=True, verbose_name="主展示图片")
    score = models.CharField(max_length=10, default="暂无评分", verbose_name="评分")
    comment_num = models.IntegerField(default=0, verbose_name="评论数")
    travelbook_num = models.IntegerField(default=0, verbose_name="攻略数")
    type = models.IntegerField(choices=TYPE_OPTION, default=1, verbose_name="分类")
    summary = models.TextField(blank=True, verbose_name="景点介绍")
    phone = models.CharField(max_length=1024, blank=True, verbose_name="联系电话")
    website = models.CharField(max_length=100, blank=True, verbose_name="网址")
    open_time = models.CharField(max_length=1024, blank=True, verbose_name="开放时间")
    ticket = models.CharField(max_length=1024, blank=True, verbose_name="门票")
    traffic = models.CharField(max_length=1024, blank=True, verbose_name="交通")
    grade = models.IntegerField(choices=GRADE_OPTION, default=1, verbose_name="景区等级")
    advice_time = models.CharField(max_length=1024, blank=True, verbose_name="建议时间")
    tips = models.TextField(blank=True, verbose_name="小提示")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_time = models.DateTimeField(auto_now=True, verbose_name="修改时间")

    class Meta:
        db_table = "mt_scene"
        verbose_name = "景区"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class SceneComment(models.Model):
    content = models.CharField(max_length=10240, verbose_name="评论内容")
    score = models.SmallIntegerField(verbose_name="评分")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="发表时间")
    user = models.ForeignKey(to=User, verbose_name="用户", on_delete=models.CASCADE)
    scene = models.ForeignKey(to=Scene, verbose_name="景点", on_delete=models.CASCADE)

    class Meta:
        db_table = "mt_scene_comment"
        verbose_name = "景点评论"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.user) + str(self.scene)
