from rest_framework.generics import ListAPIView

from .models import Carousel, NavigationBar
from mytasteapi.settings import constants
from . import serializers


class CarouselListAPIView(ListAPIView):
    """
    首页轮播图
    """
    queryset = Carousel.objects.filter(is_show=True, is_deleted=False).order_by('-orders')[:constants.CAROUSEL_LENGTH]
    serializer_class = serializers.CarouselModelSerializer

# class HeaderNavigationListAPIView(ListAPIView):
#     queryset = NavigationBar.objects.filter(position=1, is_show=True, is_deleted=
#                                             False).order_by("orders")[:constants.HEADER_NAVIGATION_LENGTH]
#     serializer_class = serializers.HeaderNavigationModelSerializer
#
#
# class FooterNavigationListAPIView(ListAPIView):
#     queryset = NavigationBar.objects.filter(position=2, is_show=True, is_deleted=
#                                             False).order_by("orders")[:constants.FOOTER_NAVIGATION_LENGTH]
#     serializer_class = serializers.FooterNavigationModelSerializer
