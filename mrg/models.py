from django.db import models
import datetime


# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    address = models.CharField(max_length=200)


class Medicine(models.Model):
    name = models.CharField(max_length=200)
    sn = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)


class Order(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    create_data = models.DateTimeField(default=datetime.datetime.now)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    medicines = models.ManyToManyField(Medicine, through='OrderMedicine')


class OrderMedicine(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    medicine = models.ForeignKey(Medicine, on_delete=models.PROTECT)
    # 订单中药品的数量
    amount = models.PositiveIntegerField
