from django.db import models

# Create your models here.
from django.core.exceptions import ObjectDoesNotExist

class Account(models.Model):
    name = models.CharField(max_length=200, unique=False)
    balance = models.DecimalField(max_digits=6, decimal_places=2)
    
    def __unicode__(self):
        return self.name
    def debit(self,sum):
        self.balance -= sum

class AccountCode(models.Model):
    account = models.ForeignKey(Account, related_name='account_codes')
    code = models.CharField(max_length=200, unique=True)
    
    def __unicode__(self):
        return u'%s - %s' % (self.account, self.code)
        
    class Meta:
        ordering = ["account"]
        
    @classmethod
    def get_or_code(self, code):
        try:
            return AccountCode.objects.get(code=code)
        except ObjectDoesNotExist:
            return code
