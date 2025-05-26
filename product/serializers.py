from rest_framework import serializers
from .models import Category, Product, Review
class CategorySerializer(serializers.ModelSerializer):
    products_count = serializers.IntegerField(read_only=True)
    class Meta:
      model = Category
      fields = '__all__'
      

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ReviewSerielizer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
class ProductWithReviewsSerializer(serializers.ModelSerializer):
    reviews = ReviewSerielizer(many=True, read_only=True)
    rating = serializers.FloatField(read_only=True)
    class Meta:
        model = Product
        fields = '__all__'