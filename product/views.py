from rest_framework.decorators import api_view
from rest_framework import generics
from .models import Category, Product, Review
from .serializers import CategorySerializer, ProductSerializer, ReviewSerielizer, ProductWithReviewsSerializer
from django.db.models import Avg, Count
class CategoryApiView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
class CategoryDetailApiView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
class ProductApiView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
class ProductDetailApiView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
class ReviewApiView(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerielizer
class ReviewDetailApiView(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerielizer

class ProductReviewsListAPIView(generics.ListAPIView):
    queryset = Product.objects.annotate(rating=Avg('reviews__stars'))
    serializer_class = ProductWithReviewsSerializer

class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.annotate(products_count=Count('product'))
    serializer_class = CategorySerializer
    