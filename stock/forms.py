from django.forms import ModelForm,forms
from models import Stock

from django.forms import ModelForm

class StockForm(ModelForm):
     class Meta:
         model = Stock

