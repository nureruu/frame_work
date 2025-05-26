from rest_framework import serializers
from .models import Category, Product, Review
class CategorySerializer(serializers.ModelSerializer):
    products_count = serializers.IntegerField(read_only=True)
    class Meta:
      model = Category
      fields = '__all__'
    def validate_title(self, value):
        if not value.strip():
            raise serializers.ValidationError("Название категории не может быть пустым.")
        if len(value) < 2:
            raise serializers.ValidationError("Название категории должно быть не короче 2 символов.")
        return value

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
    def validate_title(self, value):
        if not value.strip():
            raise serializers.ValidationError("Название товара не может быть пустым.")
        if len(value) < 3:
            raise serializers.ValidationError("Название товара должно быть не короче 3 символов.")
        return value
    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError("Цена не может быть отрицательной.")
        return value

class ReviewSerielizer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
    def validate_text(self, value):
        if not value.strip():
            raise serializers.ValidationError("Текст отзыва не может быть пустым.")
        if len(value) < 5:
            raise serializers.ValidationError("Текст отзыва должен содержать минимум 5 символов.")
        return value

    def validate_stars(self, value):
        if not (1 <= value <= 5):
            raise serializers.ValidationError("Оценка (stars) должна быть от 1 до 5.")
        return value
class ProductWithReviewsSerializer(serializers.ModelSerializer):
    reviews = ReviewSerielizer(many=True, read_only=True)
    rating = serializers.FloatField(read_only=True)
    class Meta:
        model = Product
        fields = '__all__'