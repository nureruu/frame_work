from rest_framework import serializers
from .models import Category, Product, Review
class CategorySerializer(serializers.ModelSerializer):
    model = Category
    fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    model = Product
    fields = '__all__'

class ReviewSerielizer(serializers.ModelSerializer):
    model = Review
    fields = '__all__'