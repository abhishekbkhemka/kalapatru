from datetime import timedelta

from django.db import connection
from django.utils import timezone
from rest_framework.exceptions import PermissionDenied

from LR.models import Dispatch, ForwardingNote
from LR.utils import getServerDateFromStr, dictfetchall


class DispatchController:
    def _dispatch_qs(self):
        return Dispatch.objects.prefetch_related(
            'forwardingNote__transporter',
            'forwardingNote__customer',
            'forwardingNote__company',
        )

    def lockDispatch(self, dispatch):
        dispatch.isLocked = True
        dispatch.save(update_fields=['isLocked'])

    def updateDispatch(self, request):
        params = request.data
        ds = Dispatch.objects.get(pk=params['id'])
        if ds.isLocked:
            raise PermissionDenied()
        ds.date = getServerDateFromStr(params['date'])
        ds.vanNo = params['vanNo']
        ds.name = params['name']
        ds.remarks = params.get('remarks', '')
        ds.save()

        # Clear previous links in bulk-ish fashion
        for ofn in ds.forwardingNote.all():
            ofn.isDispatched = False
            ofn.save(update_fields=['isDispatched'])
        ds.forwardingNote.clear()

        for fnId in params['forwardingNotes']:
            fn = ForwardingNote.objects.get(pk=fnId)
            fn.isDispatched = True
            fn.save(update_fields=['isDispatched'])
            ds.forwardingNote.add(fn)

        return self._dispatch_qs().get(pk=ds.pk)

    def addDispatch(self, request):
        params = request.data
        ds = Dispatch()
        ds.date = getServerDateFromStr(params['date'])
        ds.vanNo = params['vanNo']
        ds.name = params['name']
        ds.remarks = params.get('remarks', '')
        ds.save()
        for fnId in params['forwardingNotes']:
            fn = ForwardingNote.objects.get(pk=fnId)
            fn.isDispatched = True
            fn.save(update_fields=['isDispatched'])
            ds.forwardingNote.add(fn)
        return self._dispatch_qs().get(pk=ds.pk)

    def getDispatch(self, request):
        return self._dispatch_qs().get(pk=request.query_params['id'])

    def getVans(self):
        cursor = connection.cursor()
        query = (
            "SELECT vanNo, name, CONCAT(vanNo, ' ', name) as label "
            "FROM LR_dispatch GROUP BY vanNo, name"
        )
        cursor.execute(query)
        return dictfetchall(cursor)

    def getDispatches(self, request):
        params = request.query_params
        qs = self._dispatch_qs().order_by('-id')

        if 'toDate' in params and 'fromDate' in params:
            return qs.filter(
                date__range=[
                    getServerDateFromStr(params['fromDate']),
                    getServerDateFromStr(params['toDate']),
                ]
            )

        if 'fromDate' in params:
            return qs.filter(date__gte=getServerDateFromStr(params['fromDate']))

        # Never return entire history unbounded
        since = timezone.now() - timedelta(days=30)
        return qs.filter(date__gte=since)[:200]
