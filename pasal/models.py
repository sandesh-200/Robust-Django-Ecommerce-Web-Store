from django.db import models
from django.contrib.auth.models import User
import json
from django.utils import timezone
import uuid
# Create your models here

class Sale(models.Model):
    occasion = models.CharField(max_length=200)
    banner = models.ImageField(upload_to='pasal/images/banner')

    def __str__(self):
        return self.occasion

class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=200)
    product_desc = models.CharField(max_length=500)
    product_img = models.ImageField(upload_to='pasal/images/product')
    product_category = models.CharField(max_length=100)
    product_subcategory = models.CharField(max_length=100)
    price = models.IntegerField()
    publish_date = models.DateTimeField()

    def __str__(self):
        return self.product_name

class Contact(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField()
    message = models.TextField(max_length=300,blank=True)

    def __str__(self):
        return f"Message by {self.name}"
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    searched = models.CharField(max_length=60, default="")
    recommended_products = models.TextField(default="[]")

    def get_recommended_products(self):
        try:
            return json.loads(self.recommended_products)
        except ValueError:
            return []

    def add_recommended_product(self, product_id):
        products = self.get_recommended_products()
        if product_id not in products:
            products.append(product_id)
            self.recommended_products = json.dumps(products)
            self.save()

    def __str__(self):
        return self.user.username
    

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    uid = models.CharField(max_length=300, default="")
    product_id = models.CharField(max_length=100)
    product_name = models.CharField(max_length=300)
    product_price = models.IntegerField()
    product_quantity = models.IntegerField(default=0)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.product_name} by {self.user.first_name} {self.user.last_name}"
    
class Bill(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    f_name= models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=20)
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=200)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"User Bill - {self.user.first_name} {self.user.last_name}"

