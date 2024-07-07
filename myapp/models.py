from django.db import models

# Create your models here.

class Coffee(models.Model):
    name = models.CharField(max_length=255)
    amount = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    order_id = models.CharField(max_length=255)
    paid = models.BooleanField(default=False)