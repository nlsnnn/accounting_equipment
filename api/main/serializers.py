from rest_framework.serializers import ModelSerializer

from .models import Stock, Category, Equipment


class StockSerializer(ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class EquipmentSerializer(ModelSerializer):
    class Meta:
        model = Equipment
        fields = '__all__'