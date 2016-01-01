
from LR.models import Dispatch,ForwardingNote
from LR.utils import getServerDateFromStr,timeout
from rest_framework.exceptions import PermissionDenied
class DispatchController():
    def lockDispatch(self,dispatch):
        dispatch.isLocked = True
        dispatch.save()

    def updateDispatch(self,request):
        params = request.data;
        ds = Dispatch.objects.get(pk=params['id'])
        if ds.isLocked:
            raise PermissionDenied()
        ds.date = getServerDateFromStr(params['date'])
        ds.vanNo = params['vanNo']
        ds.name = params['name']
        ds.remarks = params.get('remarks','')
        fns = ds.forwardingNote.all()
        for ofn in fns:
            ofn.isDispatched = False
            ofn.save()
            ds.forwardingNote.remove(ofn)
        for fnId in params['forwardingNotes']:
            oFn = ds.forwardingNote.filter()
            fn = ForwardingNote.objects.get(pk=fnId)
            fn.isDispatched = True
            fn.save()
            ds.forwardingNote.add(fn)
            # timeout(self.lockDispatch,ds,{},10)
        return ds

    def addDispatch(self,request):
        params = request.data;
        ds = Dispatch()
        ds.date = getServerDateFromStr(params['date'])
        ds.vanNo = params['vanNo']
        ds.name = params['name']
        ds.remarks = params.get('remarks','')
        ds.save()
        for fnId in params['forwardingNotes']:
            fn = ForwardingNote.objects.get(pk=fnId)
            fn.isDispatched = True
            fn.save()
            ds.forwardingNote.add(fn)
        return ds

    def getDispatch(self,request):
        dis = Dispatch.objects.get(pk=request.query_params['id'])
        return dis


    def getDispatches(self,request):
        params = request.query_params
        if 'toDate' in params and 'fromDate' in params:
            dis = Dispatch.objects.filter(date__range=[getServerDateFromStr(params['fromDate']),getServerDateFromStr(params['toDate'])])
            return dis

        if 'fromDate' in params:
            dis = Dispatch.objects.filter(date__gte=getServerDateFromStr(params['fromDate']))
            return dis

        dis = Dispatch.objects.all()
        return dis


