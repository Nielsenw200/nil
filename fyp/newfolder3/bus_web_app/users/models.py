from django.db import models
from django.forms import CharField





from django.db import models
from bus_catalog.models import AuthUser

class Invoicing(models.Model):
    description = models.CharField(max_length=100 , null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE)
    tran_id = models.CharField(max_length=100)
    amount = models.IntegerField()
    
    
    def __str__(self):
          return f'{self.user}'