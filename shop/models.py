from decimal import Decimal
from django.db import models


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Product(TimestampedModel):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name
    

class DiscountedProduct(Product):
    class Meta:
        proxy = True

    def discounted_price(self):
        return self.price * Decimal('0.8')
    
    
class ElectronicsProduct(Product):
    brand = models.CharField(max_length=50)
    power_rating = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name} ({self.brand})"

class ClothingProduct(DiscountedProduct):
    size = models.CharField(max_length=10)
    fabric = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} ({self.size})"
