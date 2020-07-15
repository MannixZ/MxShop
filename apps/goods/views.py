from django.shortcuts import render

from .serializers import GoodSerializer
from rest_framework import mixins
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination

from rest_framework import viewsets

from .models import Goods


# Create your views here.

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = 'p'
    max_page_size = 100


class GoodsListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    商品列表页
    """
    queryset = Goods.objects.all()
    serializer_class = GoodSerializer
    pagination_class = StandardResultsSetPagination
