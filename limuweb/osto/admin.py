from django.contrib import admin
from limuweb.osto.models import Product, Barcode, Purchases, Deposits

admin.site.register(Product)
admin.site.register(Barcode)
admin.site.register(Purchases)
admin.site.register(Deposits)
