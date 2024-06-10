from rest_framework import serializers
from .models import ListProduct


class ProductsSerializers(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True)
    class Meta:
        model = ListProduct
        fields = ['id','productname', 'brand', 'category', 'stock', 'price', 'image', 'desc','seller']
