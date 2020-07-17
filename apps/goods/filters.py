#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Author  : zengmingjie  
Time    : 2020/7/17 20:25:08  
FileName: filters.py
'''

from django_filters import rest_framework as filters
from .models import Goods


class GoodsFilter(filters.filterset.FilterSet):
    """
    商品的过滤类

    """
    price_min = filters.NumberFilter(field_name='shop_price', lookup_expr='gte')
    price_max = filters.NumberFilter(field_name='shop_price', lookup_expr='lte')
    # name = filters.CharFilter(field_name='name', lookup_expr='icontains')  # 模糊搜索

    class Meta:
        model = Goods
        fields = ['price_min', 'price_max']
