from django.db import models
from django.contrib import admin
from django import forms

from django import forms
from django.contrib import admin




CHOICES = (
    ('0', 'In'),
    ('1', 'Out'),
)

class Address(models.Model):
    label = models.CharField(max_length=250, null=True, blank=True)
    cst = models.CharField(max_length=250, null=True, blank=True)
    tin = models.CharField(max_length=250, null=True, blank=True)
    address_Line1 = models.CharField(max_length=250, null=True, blank=True)
    address_Line2 = models.CharField(max_length=250, null=True, blank=True)
    city = models.CharField(max_length=250, null=True, blank=True)
    state = models.CharField(max_length=250, null=True, blank=True)
    postal_Code = models.CharField(max_length=250, null=True, blank=True)
    phone = models.CharField(max_length=250, null=True, blank=True)
    email = models.CharField(max_length=250, null=True, blank=True)
    country = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return "%s-%s" % (self.city,self.label)


admin.site.register(Address)


class Company(models.Model):
    name=models.CharField(max_length=250,null=True,blank=True)
    address=models.ManyToManyField(Address)
    def __str__(self):
        return "%s" % (self.name)


admin.site.register(Company)

class SupplyPlace(models.Model):
    name=models.CharField(max_length=250,null=True,blank=True)

    def __str__(self):
        return "%s" % (self.name)

admin.site.register(SupplyPlace)


class Commodity(models.Model):
    name=models.CharField(max_length=250,null=True,blank=True)

    def __str__(self):
        return "%s" % (self.name)

admin.site.register(Commodity)


class Stock(models.Model):
    type=models.CharField(max_length=250,choices=CHOICES)
    company=models.ForeignKey(Company)
    address=models.ForeignKey(Address)
    bill_No=models.CharField(max_length=250,null=True,blank=True)
    bill_Date=models.DateField(null=True,blank=True)
    bill_Rec_Date=models.DateField(null=True,blank=True)
    bill_Amount=models.FloatField(null=True,blank=True)
    lr_No=models.CharField(max_length=250,null=True,blank=True)
    lr_Date = models.DateField(null=True, blank=True)
    cases = models.CharField(max_length=250, null=True, blank=True)
    carriers_Name = models.CharField(max_length=250, null=True, blank=True)
    permit_No = models.CharField(max_length=250, null=True, blank=True)
    permit_Amt = models.FloatField(null=True, blank=True)
    doc_Month = models.CharField(max_length=250, null=True, blank=True)
    F_C_O=models.CharField(max_length=250, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    qrt = models.CharField(max_length=250, null=True, blank=True)
    year = models.CharField(max_length=250, null=True, blank=True)
    remarks = models.CharField(max_length=250, null=True, blank=True)
    commodity = models.ForeignKey(Commodity)


    def __str__(self):
        return "%s"%(self.company.name)


admin.site.register(Stock)


