from django.db import models
from django.contrib import admin
from django import forms

from django import forms
from django.contrib import admin




CHOICES = (
    ('0', 'In'),
    ('1', 'Out'),
)

class Stock(models.Model):
    type=models.CharField(max_length=250,choices=CHOICES)
    company_Name=models.CharField(max_length=250,null=True,blank=True)
    supply_Place=models.CharField(max_length=250,null=True,blank=True)
    bill_No=models.CharField(max_length=250,null=True,blank=True)
    bill_Date=models.DateField(null=True,blank=True)
    bill_Rec_Date=models.DateField(null=True,blank=True)
    bill_Amount=models.FloatField(null=True,blank=True)
    lr_No=models.CharField(max_length=250,null=True,blank=True)
    lr_Date = models.DateField(null=True, blank=True)
    cases = models.CharField(max_length=250, null=True, blank=True)
    carriers_Name = models.CharField(max_length=250, null=True, blank=True)
    permit_No = models.CharField(max_length=250, null=True, blank=True)
    doc_Month = models.CharField(max_length=250, null=True, blank=True)
    F_C_O=models.CharField(max_length=250, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    qrt = models.CharField(max_length=250, null=True, blank=True)
    year = models.CharField(max_length=250, null=True, blank=True)
    remarks = models.CharField(max_length=250, null=True, blank=True)
    commodity = models.CharField(max_length=250, null=True, blank=True)

# admin.site.register(Stock)

