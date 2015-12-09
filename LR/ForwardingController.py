
from LR.models import ForwardingNote,Transporter,Customer,Company
from LR.utils import getServerDateFromStr
import datetime

class ForwardingController():

    def addForwardingNote(self,request):
        params = request.data;
        fn = ForwardingNote()
        if 'billDates' in params:
            fn.billDates = ",".join(params['billDates'])
        fn.fnDate = getServerDateFromStr(params['fnDate'])
        fn.billNo = params.get('billNo','')
        fn.billValues = params['billValues']
        fn.cases = params['cases']
        if 'transporter_id' in params:
            fn.transporter_id = params['transporter_id']
        else:
            transporter = Transporter()
            transporter.name = params['transporter']['name']
            transporter.city = params['transporterStation']
            transporter.org_id = 1
            transporter.save()
            fn.transporter_id = transporter.id
        if 'customer_id' in params:
            fn.customer_id = params['customer_id']
        else:
            customer = Customer()
            customer.name = params['customer']['name']
            customer.city = params['customer']['city']
            customer.org_id =1
            customer.save()
            fn.customer_id = customer.id


        fn.marka = params['marka']
        if 'companyId' in params:
            fn.company_id = params['companyId']
        fn.transporterStation = params['transporterStation']
        fn.permitNo = params.get('permitNo','')
        fn.comments = params.get('comments','')

        fn.save()
        return fn

    def getForwardingNotes(self,request):
        params = request.query_params
        transporterName = ''
        if 'transporterName' in params:
            transporterName =  params['transporterName']
        if 'toDate' in params and 'fromDate' in params:
            fns = ForwardingNote.objects.filter(transporter__name__icontains=transporterName,fnDate__range=[getServerDateFromStr(params['fromDate']),getServerDateFromStr(params['toDate'])]).order_by('isDispatched','-fnDate')
            return fns

        if 'fromDate' in params:
            fns = ForwardingNote.objects.filter(transporter__name__icontains=transporterName,fnDate__gte=getServerDateFromStr(params['fromDate'])).order_by('isDispatched','-fnDate')
            return fns

        fns = ForwardingNote.objects.filter(transporter__name__icontains=transporterName).order_by('isDispatched','-fnDate')
        return fns


    def getForwardingNote(self,request):
        params = request.query_params
        fns = ForwardingNote.objects.get(pk=params['id'])
        return fns

    def getCompanies(self,request):
        params = request.query_params
        companies = Company.objects.filter(org_id=1)
        return companies



