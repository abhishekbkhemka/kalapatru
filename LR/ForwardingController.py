from LR.models import ForwardingNote, Customer, Company, Commodity, Station
from LR.utils import getServerDateFromStr


class ForwardingController:
    def _fn_qs(self):
        return ForwardingNote.objects.select_related(
            'transporter',
            'customer',
            'company',
            'consignor',
        )

    def addForwardingNote(self, request):
        params = request.data
        fn = ForwardingNote()
        if 'billDates' in params:
            fn.billDates = ",".join(params['billDates'])
        fn.fnDate = getServerDateFromStr(params['fnDate'])
        fn.billNo = params.get('billNo', '')
        fn.billValues = params['billValues']
        fn.cases = params['cases']
        fn.regularCases = params['regularCases']
        fn.bigCases = params['bigCases']
        fn.transporter_id = params['transporter_id']
        fn.transporterStation = params['transporterStation']
        if 'customer_id' in params:
            fn.customer_id = params['customer_id']
        else:
            try:
                customer = Customer.objects.get(
                    name__iexact=params['customer']['name'],
                    city__iexact=params['customer']['city'],
                )
            except Customer.DoesNotExist:
                customer = Customer()
                customer.name = params['customer']['name']
                customer.city = params['customer']['city']
                customer.org_id = 1
                customer.save()
            fn.customer_id = customer.id

        fn.marka = params['marka']
        if 'companyId' in params:
            fn.company_id = params['companyId']
        fn.transporterStation = params['transporterStation']
        fn.permitNo = params.get('permitNo', '')
        fn.commodity = params.get('commodity', '')

        fn.save()
        return self._fn_qs().get(pk=fn.pk)

    def getForwardingNotes(self, request):
        params = request.query_params
        transporterName = params.get('transporterName', '')
        qs = self._fn_qs().filter(
            isDispatched=False,
            transporter__name__icontains=transporterName,
        ).order_by('-id')

        if 'toDate' in params and 'fromDate' in params:
            return qs.filter(
                fnDate__range=[
                    getServerDateFromStr(params['fromDate']),
                    getServerDateFromStr(params['toDate']),
                ]
            )

        if 'fromDate' in params:
            return qs.filter(fnDate__gte=getServerDateFromStr(params['fromDate']))

        # Cap unbounded list so huge undispatched sets don't melt the API
        return qs[:500]

    def getForwardingNote(self, request):
        params = request.query_params
        return self._fn_qs().get(pk=params['id'])

    def getSettings(self, request):
        companies = Company.objects.filter(org_id=1).order_by('name')
        commodity = Commodity.objects.all().order_by('name')
        stations = Station.objects.all().order_by('label')
        return companies, commodity, stations
