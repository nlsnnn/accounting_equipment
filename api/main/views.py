from rest_framework.viewsets import ModelViewSet

from .models import Stock, Category, Equipment
from .serializers import StockSerializer, CategorySerializer, EquipmentSerializer
from .permissions import IsAdminOrRead


class StockView(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    permission_classes = [IsAdminOrRead]


class CategoryView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrRead]


class EquipmentView(ModelViewSet):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
    permission_classes = [IsAdminOrRead]