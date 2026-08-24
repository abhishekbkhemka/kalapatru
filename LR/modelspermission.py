from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from LR.constants import FORWARDINGNOTE, DISPATCH

MODEL_CHOICES = (
    (FORWARDINGNOTE, FORWARDINGNOTE),
    (DISPATCH, DISPATCH),
)


class Permission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    modelName = models.CharField(choices=MODEL_CHOICES, max_length=255)
    canCreate = models.BooleanField(default=False)
    canUpdate = models.BooleanField(default=False)
    canView = models.BooleanField(default=False)
    canDelete = models.BooleanField(default=False)
    createdDate = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updatedDate = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    createdBy = models.CharField(max_length=255, blank=True, null=True)
    updatedBy = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        unique_together = ('user', 'modelName',)


admin.site.register(Permission)
