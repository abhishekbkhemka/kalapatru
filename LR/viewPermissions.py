# __author__ = 'ganesh'

from rest_framework import permissions

class Permissions(permissions.BasePermission):
    def canView(self,request):
        model=requet.quer