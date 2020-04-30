# -*- coding:utf-8 -*-

# author:   gaoi
# datetime: 4/29/20 11:15 AM
# software: PyCharm

from django_filters import rest_framework
from .models import Hotel


class HotelFilter(rest_framework.FilterSet):
    name = rest_framework.CharFilter(field_name='name', lookup_expr='icontains', )
    ename = rest_framework.CharFilter(field_name='ename', lookup_expr='icontains')
    around = rest_framework.CharFilter(field_name='around', lookup_expr='icontains')
    address = rest_framework.CharFilter(field_name='address', lookup_expr='icontains')

    class Meta:
        model = Hotel
        fields = ['name', 'ename', 'around', 'address']
