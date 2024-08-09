from rest_framework.viewsets import ModelViewSet

from .models import Stock, Category, Equipment
from .serializers import StockSerializer, CategorySerializer, EquipmentSerializer


class StockView(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer


class CategoryView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class EquipmentView(ModelViewSet):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer