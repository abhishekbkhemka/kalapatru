
from LR.models import Dispatch,ForwardingNote
from LR.utils import getServerDateFromStr
class DispatchController():

    def addDispatch(self,request):
        params = request.data;
        ds = Dispatch()
        ds.date = getServerDateFromStr(params['date'])
        ds.vanNo = params['vanNo']
        ds.name = params['name']
        ds.remarks = params['remarks']
        ds.save()
        for fnId in params['forwardingNotes']:
            fn = ForwardingNote.objects.get(pk=fnId)
            fn.isDispatched = True
            fn.save()
            ds.forwardingNote.add(fn)
        return ds

    def getDispatches(self,request):
        params = request.query_params
        if 'toDate' in params and 'fromDate' in params:
            dis = Dispatch.objects.filter(fnDate__range=[getServerDateFromStr(params['fromDate']),getServerDateFromStr(params['toDate'])]).order_by('-date')
            return dis

        if 'fromDate' in params:
            dis = Dispatch.objects.filter(fnDate__gte=getServerDateFromStr(params['fromDate'])).order_by('-date')
            return dis

        dis = Dispatch.objects.all().order_by('-date')
        return dis
