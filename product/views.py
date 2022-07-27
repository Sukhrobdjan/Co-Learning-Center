from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Product,Category,Comment,Option,OptionValue,ProductImage
from common.models import User
from .serializers import CommentSerializer, ProductSerializer
# CategorySerializer, CommentSerializer
# ProductImageSerializer.CategorySerializer,CommentSerializer
from helpers.pagination import CustomPagination
# from rest_framework.pagination import LimitOffsetPagination


class ProductViewSet(ListAPIView):
    queryset = Product.objects.all().select_related('category')
    serializer_class = ProductSerializer
    pagination_class = CustomPagination

class CommentViewSet(ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
