from django.contrib import admin
from limuweb.osto.models import Product, Barcode, Purchase

class ProductAdmin(admin.ModelAdmin):
	list_display = ('name','current_price')
#	exclude = ('',)
#	search_fields = ('',)
#	date_hierarchy = ''
#	inlines = []

admin.site.register(Product, ProductAdmin)

class BarcodeAdmin(admin.ModelAdmin):
	list_display = ('product','code')
#	exclude = ('',)
#	search_fields = ('',)
#	date_hierarchy = ''
#	inlines = []

admin.site.register(Barcode, BarcodeAdmin)

class PurchaseAdmin(admin.ModelAdmin):
	list_display = ('user','product','price','created')
#	exclude = ('',)
#	search_fields = ('',)
#	date_hierarchy = ''
#	inlines = []

admin.site.register(Purchase, PurchaseAdmin)
