from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Inseam(models.Model):
    value = models.IntegerField(unique=True)  # فاق

    def __str__(self):
        return str(self.value)

class Diameter(models.Model):
    value = models.IntegerField(unique=True)  # سایز

    def __str__(self):
        return str(self.value)

class Width(models.Model):
    value = models.IntegerField(unique=True)  # عرض

    def __str__(self):
        return str(self.value)

class Product(models.Model):
    #artist = models.ForeignKey(Musician, on_delete=models.CASCADE)

    product_name = models.CharField(max_length=200)
    product_brandname = models.CharField(max_length=100,default='')
    product_contry = models.CharField(max_length=100,default='ایران')
    product_number = models.IntegerField()
    product_price = models.IntegerField(default=0)
    product_stock = models.IntegerField(default=0)
    product_view = models.IntegerField(default=0)
    product_width=models.IntegerField(default=0)
    product_Diameter=models.FloatField(default=0)
    product_layer=models.IntegerField(default=0)
    product_weight=models.IntegerField(default=0)
    product_speed=models.IntegerField(default=0)
    product_discountpercent_total=models.IntegerField(default=0)
    product_discountpercent_this = models.IntegerField(default=0)
    product_discount_price = models.IntegerField(default=0)
    product_profitpercent = models.IntegerField(default=0)
    product_price_final = models.IntegerField(default=0)
    product_type=models.CharField(max_length=100,default='سواری')
    product_car_type=models.CharField(max_length=100,default='پژو')
    product_model=models.CharField(max_length=100,default='206')
    product_garanty_year=models.IntegerField(default=0)
    product_create_year = models.IntegerField(default=0)
    product_image = models.ImageField(blank=True,upload_to='product/')

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()  # مثلا 1 تا 5
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    optional_name = models.CharField(max_length=100, blank=True, null=True)  # نام اختیاری

    def __str__(self):
        return f'{self.user.username} - {self.product.name}'






