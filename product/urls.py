from django.urls import path
from .views import *
urlpatterns = [
    path('categories/', CategoryApiView.as_view()),
    path('categories/<int:id>/', CategoryDetailApiView.as_view()),
    path('products/', ProductApiView.as_view()),
    path('products/<int:id>/', ProductDetailApiView.as_view()),
    path('reviews/', ReviewApiView.as_view()),
    path('reviews/<int:id>/', ReviewDetailApiView.as_view()),
    path('api/v1/products/reviews/', ProductReviewsListAPIView.as_view()),
    path('api/v1/categories/', CategoryListAPIView.as_view()),
]
