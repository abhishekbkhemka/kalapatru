
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