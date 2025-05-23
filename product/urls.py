from .views import *
from django.urls import path
urls = [
    path('/api/v1/categories/', CategoryApiView.as_view()),
    path('/api/v1/categories/<int:id>/', CategoryDetailApiView.as_view()),
    path('/api/v1/products/', ProductApiView.as_view()),
    path('/api/v1/products/<int:id>/', ProductDetailApiView.as_view()),
    path('/api/v1/reviews/', ReviewApiView.as_view()),
    path('/api/v1/reviews/<int:id>/', ReviewDetailApiView.as_view()),
]
