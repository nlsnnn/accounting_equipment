from django.db import models


class Stock(models.Model):
    name = models.CharField(verbose_name='Название', max_length=250)
    address = models.CharField(verbose_name='Адресс', max_length=250)
    capacity = models.PositiveIntegerField(verbose_name='Вместимость')
    time_created = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    time_updated = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)


class Category(models.Model):
    name = models.CharField(verbose_name='Название', max_length=250)
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    time_created = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    time_updated = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)


class Equipment(models.Model):
    name = models.CharField(verbose_name='Навзание', max_length=250)
    cat = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Категория')
    stock = models.ForeignKey(Stock, on_delete=models.PROTECT, verbose_name='Склад')
    time_created = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    time_updated = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)