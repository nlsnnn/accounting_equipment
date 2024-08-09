from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import StockView, CategoryView, EquipmentView


router = DefaultRouter()
router.register('stock', StockView)
router.register('cat', CategoryView)
router.register('equipment', EquipmentView)

urlpatterns = [
    path('', include(router.urls))
]