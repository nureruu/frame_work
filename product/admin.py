from django.contrib import admin
from .models import Product, Review, Category

class ReviewInline(admin.StackedInline):
    model = Review
    extra = 0

class ProductAdmin(admin.ModelAdmin):
    inlines = [ReviewInline]

admin.site.register(Product, ProductAdmin)
admin.site.register(Review)
admin.site.register(Category)
