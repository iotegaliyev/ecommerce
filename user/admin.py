from django.contrib import admin
from .models import CustomerProfile, SellerProfile

# Register your models here.
admin.site.register(CustomerProfile)
admin.site.register(SellerProfile)
