from django.db import models

from mytasteapi.utils.models import Base


# Create your models here.
class Carousel(Base):
    """
    首页广告轮播图模型
    """
    title = models.CharField(max_length=500, verbose_name="广告标题")
    link = models.CharField(max_length=500, verbose_name="广告链接")
    # 设置轮播图保存的子文件夹
    image_url = models.ImageField(upload_to="carousel", max_length=255, verbose_name="图片")
    remark = models.TextField(verbose_name="备注信息")

    class Meta:
        db_table = "mt_carousel"
        verbose_name = "轮播广告"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class NavigationBar(Base):
    """
    导航菜单模型
    """
    POSITION_OPTION = (
        (1, "顶部导航"),
        (2, "脚部导航")
    )
    title = models.CharField(max_length=500, verbose_name="导航标题")
    link = models.CharField(max_length=500, verbose_name="导航链接")
    position = models.IntegerField(choices=POSITION_OPTION, verbose_name="导航位置")
    is_site = models.BooleanField(default=False, verbose_name="是否站外跳转")

    class Meta:
        db_table = "mt_navigation"
        verbose_name = "导航条"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
