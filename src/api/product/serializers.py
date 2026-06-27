from rest_framework import serializers
from apps.product.models import Product, Category 

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name_uz', 'name_ru', 'is_active']


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.filter(is_active=True), 
        source='category', 
        write_only=True
    )

    class Meta:
        model = Product
        fields = [
            'id', 'category', 'category_id', 
            'name_uz', 'name_ru', 
            'price', 
            'desc_uz', 'desc_ru', 
            'is_active', 'image'
        ]