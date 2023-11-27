from django.db import models
from django.contrib.auth.models import User


class CustomerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.user.username


class SellerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return self.user.username
