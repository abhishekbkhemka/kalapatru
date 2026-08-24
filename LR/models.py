from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

from LR.utils import validate_json

COUNTRY = (
    ('IN', 'India'),
)

STATE = (
    ('BR', 'Bihar'),
)


class ResetId(models.Model):
    forwardingNoteId = models.BigIntegerField(null=True, blank=True)
    dispatchId = models.BigIntegerField(null=True, blank=True)


class Address(models.Model):
    addressLine1 = models.CharField(max_length=250, blank=True, null=True)
    addressLine2 = models.CharField(max_length=250, blank=True, null=True)
    area = models.CharField(max_length=250, blank=True, null=True)
    city = models.CharField(max_length=250)
    state = models.CharField(max_length=250, choices=STATE, blank=True, null=True)
    country = models.CharField(max_length=250, choices=COUNTRY, blank=True, null=True)

    def __str__(self):
        return "%s ,%s ,%s -%s %s " % (
            self.addressLine1, self.addressLine2, self.area, self.city, self.state
        )


class Organization(models.Model):
    name = models.CharField(max_length=250)
    user = models.ManyToManyField(User)

    def __str__(self):
        return " %s " % (self.name)


class Company(Address):
    org = models.ForeignKey(Organization, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    code = models.CharField(max_length=250)
    vat = models.CharField(max_length=250, default=True, null=True)
    cst_or_tin = models.CharField(max_length=250, default=True, null=True)

    def __str__(self):
        return "%s" % (self.name)


class Station(Address):
    label = models.CharField(max_length=250)

    def save(self, *args, **kwargs):
        self.label = str(self.city)
        super().save(*args, **kwargs)

    def __str__(self):
        return " %s " % (self.label)


class Transporter(Address):
    org = models.ForeignKey(Organization, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    contactNumber = models.CharField(max_length=250, blank=True, null=True)
    contactPerson = models.CharField(max_length=250, blank=True, null=True)
    isActive = models.BooleanField(default=True)
    label = models.CharField(max_length=255, blank=True, null=True)
    stations = models.ManyToManyField(Station)

    class Meta:
        verbose_name = "Consignor"
        ordering = ('name',)

    def save(self, *args, **kwargs):
        self.label = str(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return " %s " % (self.label)


class Consignor(Address):
    org = models.ForeignKey(Organization, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    contactNumber = models.BigIntegerField()
    contactPerson = models.CharField(max_length=250, blank=True, null=True)
    isActive = models.BooleanField(default=True)
    logo = models.ImageField(blank=True, null=True)

    def __str__(self):
        return "%s 's %s" % (self.name, self.org.name)

    class Meta:
        verbose_name = "Consignor"
        ordering = ('name',)


class Customer(models.Model):
    org = models.ForeignKey(Organization, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    contactNumber = models.BigIntegerField(blank=True, null=True)
    contactPerson = models.CharField(max_length=250, blank=True, null=True)
    tin = models.CharField(max_length=250, blank=True, null=True)
    isActive = models.BooleanField(default=True)
    label = models.CharField(max_length=255, blank=True, null=True)
    addressLine1 = models.CharField(max_length=250, blank=True, null=True)
    addressLine2 = models.CharField(max_length=250, blank=True, null=True)
    area = models.CharField(max_length=250, blank=True, null=True)
    city = models.CharField(max_length=250, blank=True, null=True)
    state = models.CharField(max_length=250, choices=STATE, blank=True, null=True)
    country = models.CharField(max_length=250, choices=COUNTRY, blank=True, null=True)

    class Meta:
        verbose_name = "Customers"
        ordering = ('name',)

    def save(self, *args, **kwargs):
        self.label = str(self.name) + ' ' + str(self.contactNumber) + ' ' + str(self.contactPerson)
        super().save(*args, **kwargs)

    def __str__(self):
        return "%s -(%s) In %s" % (self.name, self.contactNumber, self.org.name)


class ForwardingNote(models.Model):
    billDates = models.CharField(max_length=250, blank=True, null=True)
    transporter = models.ForeignKey(Transporter, on_delete=models.CASCADE)
    transporterStation = models.CharField(max_length=250, blank=True, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    createdDate = models.DateTimeField(auto_now_add=True)
    billNo = models.CharField(max_length=250, blank=True, null=True)
    billValues = models.CharField(max_length=250, blank=True, null=True)
    cases = models.CharField(max_length=250, blank=True, null=True)
    regularCases = models.CharField(max_length=250, blank=True, null=True)
    bigCases = models.CharField(max_length=250, blank=True, null=True)
    marka = models.CharField(max_length=250, blank=True, null=True)
    permitNo = models.CharField(max_length=250, blank=True, null=True)
    consignor = models.ForeignKey(Consignor, on_delete=models.SET_NULL, blank=True, null=True)
    commodity = models.CharField(max_length=250, blank=True, null=True)
    isDispatched = models.BooleanField(default=False)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, blank=True, null=True)
    fnDate = models.DateTimeField()
    slug = models.BigIntegerField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.pk is None:
            try:
                rObj = ResetId.objects.all().order_by("-id")[0]
                newSlug = rObj.forwardingNoteId + 1 if rObj.forwardingNoteId else 1
            except Exception:
                rObj = ResetId()
                newSlug = 1
            self.slug = newSlug
            rObj.forwardingNoteId = newSlug
            rObj.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return "%s -marka -%s on date:- %s" % (self.id, self.marka, self.fnDate)


class Dispatch(models.Model):
    date = models.DateTimeField()
    forwardingNote = models.ManyToManyField(ForwardingNote)
    vanNo = models.CharField(max_length=250, blank=True, null=True)
    name = models.CharField(max_length=250, blank=True, null=True)
    remarks = models.CharField(max_length=250, blank=True, null=True)
    isLocked = models.BooleanField(default=True)
    slug = models.BigIntegerField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.pk is None:
            try:
                rObj = ResetId.objects.all().order_by("-id")[0]
                newSlug = rObj.dispatchId + 1 if rObj.dispatchId else 1
            except Exception:
                rObj = ResetId()
                newSlug = 1
            self.slug = newSlug
            rObj.dispatchId = newSlug
            rObj.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return "%s is Disparch on %s" % (self.name, self.date)

    class Meta:
        verbose_name = "Dispatche"


class Commodity(models.Model):
    label = models.CharField(max_length=250, blank=True, null=True)
    name = models.CharField(max_length=250)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return " %s " % (self.name)


class DailyReport(models.Model):
    purchase_detail = models.TextField(default='[]', blank=True, null=True, validators=[validate_json])
    expenses_detail = models.TextField(default='[]', blank=True, null=True, validators=[validate_json])
    misc_cash_in_details = models.TextField(default='[]', blank=True, null=True, validators=[validate_json])
    day_card_sale = models.FloatField(blank=True, null=True, default=0)
    bank_deposit = models.FloatField(blank=True, null=True, default=0)
    day_credit_sale = models.FloatField(blank=True, null=True, default=0)
    total_expense = models.FloatField(blank=True, null=True, default=0)
    total_credit_purchase = models.FloatField(blank=True, null=True, default=0)
    total_cash_purchase = models.FloatField(blank=True, null=True, default=0)
    opening_balance = models.FloatField(blank=True, null=True, default=0)
    total_misc_cash_in = models.FloatField(blank=True, null=True, default=0)
    cash_inhand = models.FloatField(blank=True, null=True, default=0)
    date = models.DateField(blank=True, null=True)
    day_cash_sale = models.FloatField(blank=True, null=True, default=0)
    branch_name = models.CharField(max_length=50, blank=True, null=True)
    day_cash_difference = models.FloatField(blank=True, null=True, default=0)
    is_editable = models.BooleanField(default=False)


admin.site.register(Transporter)
admin.site.register(Consignor)
admin.site.register(Station)
admin.site.register(Customer)
admin.site.register(ForwardingNote)
admin.site.register(Dispatch)
admin.site.register(Organization)
admin.site.register(Company)
admin.site.register(Commodity)
admin.site.register(ResetId)
