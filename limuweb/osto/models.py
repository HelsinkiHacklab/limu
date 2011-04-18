from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
	name = models.CharField(max_length=200)
	current_price = models.DecimalField(max_digits = 4, decimal_places=2)

class Barcode(models.Model):
	product = models.ForeignKey(Product, related_name='barcodes')
	code = models.CharField(max_length=200)

class Purchase(models.Model):
	user = models.ForeignKey(User, related_name='purchases')
	product = models.ForeignKey(Product, related_name='purchases')
	price = models.DecimalField(max_digits = 4, decimal_places=2)
