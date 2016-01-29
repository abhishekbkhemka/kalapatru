# __author__ = 'ganesh'
from django.contrib.auth.decorators  import login_required
from django.http import HttpResponse,HttpResponseNotAllowed
from modelspermission import *
from rest_framework.views import APIView
from rest_framework import status

def permitted_actions(action = None,module= None):
    def func_wrapper(func):
        def func_handler(*args,**kwargs):
            usr=args[0].user
            method=args[0].method
            perObj=Permission.objects.get(user=usr,modelName=module)
            if method in action and perObj.canView:
                 return func(*args,**kwargs)
            else:
                res = HttpResponse("Not allowed")
                res.status_code = status.HTTP_403_FORBIDDEN
                return  res
        return func_handler
    return func_wrapper



