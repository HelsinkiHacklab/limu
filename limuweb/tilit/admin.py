from django.contrib import admin
from limuweb.tilit.models import Account, AccountCode

class AccountAdmin(admin.ModelAdmin):
	list_display = ('name','balance')
#	exclude = ('',)
#	search_fields = ('',)
#	date_hierarchy = ''
#	inlines = []

admin.site.register(Account, AccountAdmin)

class AccountCodeAdmin(admin.ModelAdmin):
	list_display = ('account','code')
#	exclude = ('',)
#	search_fields = ('',)
#	date_hierarchy = ''
#	inlines = []

admin.site.register(AccountCode, AccountCodeAdmin)
