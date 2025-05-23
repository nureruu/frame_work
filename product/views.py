from rest_framework.decorators import api_view
from rest_framework import generics
from .models import Category, Product, Review
from .serializers import CategorySerializer, ProductSerializer, ReviewSerielizer
class CategoryApiView(generics.ListAPIView):
    set = Category.objects.all()
    serializer_class = CategorySerializer
class CategoryDetailApiView(generics.ListAPIView):
    set = Category.objects.all()
    serializer_class = CategorySerializer
class ProductApiView(generics.ListAPIView):
    set = Product.objects.all()
    serializer_class = ProductSerializer
class ProductDetailApiView(generics.ListAPIView):
    set = Product.objects.all()
    serializer_class = ProductSerializer
class ReviewApiView(generics.ListAPIView):
    set = Review.objects.all()
    serializer_class = ReviewSerielizer
class ReviewDetailApiView(generics.ListAPIView):
    set = Review.objects.all()
    serializer_class = ReviewSerielizer