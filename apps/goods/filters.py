#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Author  : zengmingjie  
Time    : 2020/7/17 20:25:08  
FileName: filters.py
'''

from django_filters import rest_framework as filters
from django.db.models import Q

from .models import Goods


class GoodsFilter(filters.filterset.FilterSet):
    """
    商品的过滤类

    """
    pricemin = filters.NumberFilter(field_name='shop_price', lookup_expr='gte')
    pricemax = filters.NumberFilter(field_name='shop_price', lookup_expr='lte')
    top_category = filters.NumberFilter(method='top_category_filter')
    # name = filters.CharFilter(field_name='name', lookup_expr='icontains')  # 模糊搜索

    def top_category_filter(self, queryset, name, value):
        return queryset.filter(Q(category_id=value) | Q(category__parent_category_id=value) | Q(category__parent_category_id__parent_category_id=value))


    class Meta:
        model = Goods
        fields = ['pricemin', 'pricemax']
