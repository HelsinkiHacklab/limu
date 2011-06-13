from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

# Create your models here.

class Product(models.Model):
	name = models.CharField(max_length=200, unique=True)
	current_price = models.DecimalField(max_digits = 6, decimal_places=2) # 9999.99e maximum
	image = models.ImageField(upload_to='product', blank=True, null=True)
	
	def __unicode__(self):
		return self.name

	class Meta:
		ordering = ["name"]

class Barcode(models.Model):
	product = models.ForeignKey(Product, related_name='barcodes')
	code = models.CharField(max_length=200, unique=True)
	
	def __unicode__(self):
		return u'%s - %s' % (self.product, self.code)

	class Meta:
		ordering = ["product"]

	@classmethod
	def get_or_code(self, code):
		try:
			return Barcode.objects.get(code=code)
		except ObjectDoesNotExist:
			return code

class Purchase(models.Model):
	user = models.ForeignKey(User, related_name='purchases')
	product = models.ForeignKey(Product, related_name='purchases')
	price = models.DecimalField(max_digits = 6, decimal_places=2, blank=True)
	created = models.DateTimeField(auto_now_add = True)

	def __unicode__(self):
		return u'%s bought %s for %.2fe' % (self.user, self.product, self.price)
	
	def save(self, *args, **kwargs):
		if self.price == None or self.price == '':
			self.price = self.product.current_price
		super(Purchase, self).save(*args, **kwargs)
