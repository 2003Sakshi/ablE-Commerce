from django.db import models
from .category import Category
from .customer import Customer
from .orders import Order
from .product import Product

class Delivery(models.Model):
    objects = None
    product_name = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_price = models.ForeignKey(Order,on_delete=models.CASCADE)
    product_quantity = models.ForeignKey(Order, on_delete=models.CASCADE, default = 1)
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE,default=1)
    customer_name = models.ForeignKey(Customer, on_delete=models.CASCADE, default = 1)
    customer_address = models.ForeignKey(Order, on_delete=models.CASCADE, default = 1)
    customer_phone = models.ForeignKey(Order,on_delete=models.CASCADE)

    @staticmethod
    def get_delivery_by_id(ids):
        return Delivery.objects.filter(id__in=ids)

    @staticmethod
    def get_all_deliveries():
        return Delivery.objects.all()

    @staticmethod
    def get_all_deliveries_by_category_id(category_id):
        if category_id:
            return Delivery.objects.filter(category = category_id)
        else:
            return Delivery.get_all_deliveries()

    @staticmethod
    def get_all_deliveries_by_customer_id(customer_id):
        if customer_id:
            return Delivery.objects.filter(category=customer_id)
        else:
            return Delivery.get_all_deliveries()
