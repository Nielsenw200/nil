from dataclasses import fields
from pyexpat import model
import django_filters

from .models import *


class BusFilter(django_filters.FilterSet):
     class Meta:
         model= Assigntrip 
         fields='__all__'
     
