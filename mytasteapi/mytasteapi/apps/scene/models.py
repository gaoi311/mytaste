from django.db import models

class Province(models.Model):
    name = models.CharField(max_length=50, verbose_name="省份")

    class Meta:
        db_table = 'mt_province'
        verbose_name = "省份"
        verbose_name_plural = verbose_name


class City(models.Model):
    city_index = models.IntegerField(verbose_name="省属市索引")
    province = models.ForeignKey(to=Province, on_delete=models.CASCADE, verbose_name="所在省")
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'mt_city'
        verbose_name = "地级市"
        verbose_name_plural = verbose_name


'''
‘dest_id’(景点ID), ‘dest_name’(景点名称), ‘dest_en_name’(景点英文名称), ‘navigation_bar’(导航栏), 
‘real_city’(真实城市), ‘city’(所在城市或地区), ‘special_remind’(特别提醒), ‘photos’(景点图片链接), 
‘score’(评分), ‘ranking’(景点排名), ‘recommend_playtime’(建议游玩时间), ‘comment_num’(点评数), 
‘lat’(纬度), ‘lng’(经度), ‘percent’(占来本市驴友的百分比), ‘travelbook_num’(旅行攻略数),
‘summary_description’(景点概述), ‘address’(地址), ‘phone’(电话), ‘website’(网站), 
‘opening_hours’(开放时间), ‘admission_ticket’(门票),‘tourist_season’(旅游时节), 
‘traffic_guide’(交通指南), ‘tips’(小贴士), ‘grade’(景点等级), 
‘time_reference’(用时参考), ‘url’(景点详情页链接) 
'''


class Scene(models.Model):
    TYPE_OPTION = (
        (1, "其他"),
        (2, "自然"),
        (3, "文化"),
        (4, "历史"),
        (5, "建筑"),
        (6, "公园")
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
