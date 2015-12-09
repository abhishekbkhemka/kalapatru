from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User



# Create your models here.
COUNTRY = (
    ('IN', 'India'),
)

STATE = (
    ('BR', 'Bihar'),
)





class Address(models.Model):
    addressLine1 = models.CharField(max_length=250,blank=True,null=True)
    addressLine2 = models.CharField(max_length=250,blank=True,null=True)
    area = models.CharField(max_length=250,blank=True,null=True)
    city = models.CharField(max_length=250)
    state = models.CharField(max_length=250,choices=STATE,blank=True,null=True)
    country = models.CharField(max_length=250,choices=COUNTRY,blank=True,null=True)

    def __str__(self):
        return "%s ,%s ,%s -%s %s "%(self.addressLine1,self.addressLine2,self.area,self.city,self.state)

class Organization(models.Model):
    name = models.CharField(max_length=250)
    user = models.ManyToManyField(User)

    def __str__(self):
        return " %s "%(self.name)

class Company(Address):
    org = models.ForeignKey(Organization)
    name = models.CharField(max_length=250)
    code = models.CharField(max_length=250)

    def __str__(self):
        return "%s"%(self.name)













class Station(Address):
    label = models.CharField(max_length=250)
    def save(self, *args, **kwargs):
        self.label = str(self.city)
        super(Station, self).save(*args, **kwargs)
    def __str__(self):
        return " %s "%(self.label)

class Transporter(Address):
    org = models.ForeignKey(Organization)
    name = models.CharField(max_length=250)
    contactNumber = models.BigIntegerField(blank=True,null=True)
    contactPerson = models.CharField(max_length=250,blank=True,null=True)
    isActive = models.BooleanField(default=True)
    label = models.CharField(max_length=255,blank=True,null=True)
    stations = models.ManyToManyField(Station)

    def save(self, *args, **kwargs):
        self.label = str(self.name) + ' ' +str(self.contactNumber) + ' of '+ str(self.contactPerson)
        super(Transporter, self).save(*args, **kwargs)

    def __str__(self):
        return " %s "%(self.label)



class Consignor(Address):
    org = models.ForeignKey(Organization)
    name = models.CharField(max_length=250)
    contactNumber = models.IntegerField()
    contactPerson = models.CharField(max_length=250,blank=True,null=True)
    isActive = models.BooleanField(default=True)
    logo = models.ImageField(blank=True,null=True)

    def __str__(self):
        return "%s 's %s"%(self.name,self.org.name)



    class Meta:
         verbose_name = "Consignor"



class Customer(Address):
    org = models.ForeignKey(Organization)
    name = models.CharField(max_length=250)
    contactNumber = models.BigIntegerField(blank=True,null=True)
    contactPerson = models.CharField(max_length=250,blank=True,null=True)
    isActive = models.BooleanField(default=True)
    label = models.CharField(max_length=255,blank=True,null=True)

    def save(self, *args, **kwargs):
        self.label = str(self.name) + ' ' +str(self.contactNumber) + ' '+ str(self.contactPerson)
        super(Customer, self).save(*args, **kwargs)

    def __str__(self):
        return "%s -(%s) In %s"%(self.name,self.contactNumber,self.org.name)


class ForwardingNote(models.Model):
    billDates = models.CharField(max_length=250,blank=True,null=True)
    transporter = models.ForeignKey(Transporter)
    transporterStation = models.CharField(max_length=250,blank=True,null=True)
    customer = models.ForeignKey(Customer)
    # customerStation = models.OneToOneField(Station)
    createdDate = models.DateTimeField(auto_now_add=True)
    billNo = models.CharField(max_length=250,blank=True,null=True)
    billValues = models.CharField(max_length=250,blank=True,null=True)
    cases = models.CharField(max_length=250,blank=True,null=True)
    marka = models.CharField(max_length=250,blank=True,null=True)
    permitNo = models.CharField(max_length=250,blank=True,null=True)
    consignor = models.ForeignKey(Consignor,blank=True,null=True)
    comments =models.CharField(max_length=250,blank=True,null=True)
    isDispatched = models.BooleanField(default=False)
    company  = models.ForeignKey(Company,blank=True,null=True)
    fnDate = models.DateTimeField()

    def __str__(self):
        return "marka -%s on date:- %s"%(self.marka,self.fnDate)



class Dispatch(models.Model):
    date = models.DateTimeField()
    forwardingNote = models.ManyToManyField(ForwardingNote)
    vanNo = models.CharField(max_length=250,blank=True,null=True)
    name = models.CharField(max_length=250,blank=True,null=True)
    remarks = models.CharField(max_length=250,blank=True,null=True)
    isLocked = models.BooleanField(default=False)

    def __str__(self):
        return "%s is Disparch on %s"%(self.name,self.date)




admin.site.register(Transporter)
admin.site.register(Consignor)
admin.site.register(Station)
admin.site.register(Customer)
admin.site.register(ForwardingNote)
admin.site.register(Dispatch)
admin.site.register(Organization)
admin.site.register(Company)
# admin.site.register(Address)
