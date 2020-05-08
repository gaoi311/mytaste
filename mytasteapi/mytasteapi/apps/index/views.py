from rest_framework.generics import ListAPIView

from .models import Carousel
from mytasteapi.settings import constants
from . import serializers


class CarouselListAPIView(ListAPIView):
    """
    首页轮播图
    """
    queryset = Carousel.objects.filter(is_show=True, is_deleted=False).order_by('-orders')[:constants.CAROUSEL_LENGTH]
    serializer_class = serializers.CarouselModelSerializer
