from django.contrib import admin
from .models import Sale,Product,Bill,Contact,Profile,Order

# Register your models here.
admin.site.register(Sale)
admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(Profile)
admin.site.register(Order)
admin.site.register(Bill)
