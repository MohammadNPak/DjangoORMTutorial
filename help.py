from shop.models import Product

# seting up models
# models.py
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name


# Creating a new product and saving it to the database
new_product = Product(name="Widget", price=9.99, description="A small widget.")
new_product.save()

# Querying the database to get all products with a price less than 20
cheap_products = Product.objects.filter(price__lt=20)

# Updating a product and saving the changes to the database
product = Product.objects.get(name="Widget")
product.price = 12.99
product.save()

# Deleting a product from the database
product = Product.objects.get(name="Widget")
product.delete()






# Querying data using filters
products = Product.objects.filter(price__lt=20)

# Chaining filters
cheap_widgets = Product.objects.filter(category="Widgets").filter(price__lt=20)

# Executing database queries
for product in products:
    print(product.name)







# Creating new records (objects)
new_product = Product(name="Widget", price=9.99, description="A small widget.")
new_product.save()

# Retrieving data from the database
product = Product.objects.get(name="Widget")

# Updating records in the database
product.price = 12.99
product.save()

# Deleting records from the database
product.delete()





from django.db.models import Avg, Count, Min, Max, Sum
# Aggregation functions
average_price = Product.objects.aggregate(avg_price=Avg('price'))
total_products = Product.objects.count()
total_price = Product.objects.aggregate(total_price=Sum('price'))





# Foreign Key Relationships python

class Category(models.Model):
    name = models.CharField(max_length=100)

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)





# One-to-One and Many-to-Many Relationships
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Product(models.Model):
    name = models.CharField(max_length=100)
    categories = models.ManyToManyField(Category)



# Related Managers and Query Optimization

# Accessing related objects using managers
category = Category.objects.get(name="Electronics")
electronics_products = category.product_set.all()

# Using select_related for query optimization
products = Product.objects.select_related('category').filter(category__name="Electronics")





# Proxy Models  

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

class DiscountedProduct(Product):
    class Meta:
        proxy = True

    def discounted_price(self):
        return self.price * 0.8





# Abstract Models
class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Product(TimestampedModel):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)




# Multi-table Inheritance
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

class DiscountedProduct(Product):
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2)
