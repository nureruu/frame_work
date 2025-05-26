from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
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
    
class CategoryListCreateView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'id'

class ProductListCreateView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'

class ReviewListCreateView(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerielizer

class ReviewDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerielizer
    lookup_field = 'id'