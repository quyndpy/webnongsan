from django.contrib.auth.models import User
from django.db import models

# Create your models here.
CATEGORY_CHOICES = (
    ('HDD', 'Hạt dinh dưỡng'),
    ('RCQ', 'Rau củ quả'),
    ('TTD', 'Trà thảo dược'),
)


class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    composition = models.TextField(default='')
    prodapp = models.TextField(default='')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=3)
    product_image = models.ImageField(upload_to='product')
    def __str__(self):
        return self.title

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    mobile = models.IntegerField(default=0)
    zipcode = models.IntegerField()

    def __str__(self):
        return self.name