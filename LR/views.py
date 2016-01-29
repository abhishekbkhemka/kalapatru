from django.shortcuts import render
from rest_framework.decorators import api_view
from LR.TransporterCtl import TransporterController
from LR.CustomerCtl import CustomerController
from LR.ForwardingController import ForwardingController
from LR.DispatchController import DispatchController
from django.http import HttpResponse
from LR.Serializers import TransporterSerializer,StationsSeializers,CustomerSerializer,ForwardingSerializer,DispatchSerializer,ForwardingDetailSerializer,CompanySerializer,CommoditySeializers
from rest_framework.renderers import JSONRenderer
from rest_framework.exceptions import PermissionDenied





# Create your views here.

@api_view(['GET'])
def transporters(request, **arg):
    try:
        ctrl = TransporterController()
        retData = ctrl.getTransporters(request.user)
        result = TransporterSerializer(retData,many=True).data
        return HttpResponse(JSONRenderer().render(result))
    except Exception,e:
        from rest_framework import status
        res = HttpResponse(e)
        res.status_code = status.HTTP_403_FORBIDDEN
        return res

@api_view(['GET'])
def customers(request, **arg):
    try:
        ctrl = CustomerController()
        retData = ctrl.getCustomers(request.user)
        result = CustomerSerializer(retData,many=True).data
        return HttpResponse(JSONRenderer().render(result))
    except Exception,e:
        from rest_framework import status
        res = HttpResponse(e)
        res.status_code = status.HTTP_403_FORBIDDEN
        return res

@api_view(['GET'])
def settings(request, **arg):
    try:
        ctrl = ForwardingController()
        companies,commodity,stations = ctrl.getSettings(request)
        companies = CompanySerializer(companies,many=True).data
        commodity = CommoditySeializers(commodity,many=True).data
        stations = StationsSeializers(stations,many=True).data
        result = {}
        result['companies'] = companies
        result['commodities'] = commodity
        result['stations'] = stations
        return HttpResponse(JSONRenderer().render(result))
    except Exception,e:
        from rest_framework import status
        res = HttpResponse(e)
        res.status_code = status.HTTP_403_FORBIDDEN
        return res

@api_view(['POST','GET'])
def forwardingNote(request,**args):
    try:
        if request.method == 'POST':
            ctrl = ForwardingController()
            retData = ctrl.addForwardingNote(request)
            result = ForwardingSerializer(retData).data
            return HttpResponse(JSONRenderer().render(result))

        if request.method == 'GET':
            ctrl = ForwardingController()
            retData = ctrl.getForwardingNote(request)
            result = ForwardingDetailSerializer(retData).data
            return HttpResponse(JSONRenderer().render(result))
    except Exception,e:
        from rest_framework import status
        res = HttpResponse(e)
        res.status_code = status.HTTP_403_FORBIDDEN
        return res

@api_view(['GET'])
def forwardingNotes(request,**args):
    try:
        ctrl = ForwardingController()
        retData = ctrl.getForwardingNotes(request)
        result = ForwardingDetailSerializer(retData,many=True).data
        return HttpResponse(JSONRenderer().render(result))
    except Exception,e:
        from rest_framework import status
        res = HttpResponse(e)
        res.status_code = status.HTTP_403_FORBIDDEN
        return res


@api_view(['POST','GET','PUT'])
def dispatch(request,**args):
    if request.method == 'POST':
        try:
            ctrl = DispatchController()
            retData = ctrl.addDispatch(request)
            result = DispatchSerializer(retData).data
            return HttpResponse(JSONRenderer().render(result))
        except Exception,e:
            from rest_framework import status
            res = HttpResponse(e)
            res.status_code = status.HTTP_403_FORBIDDEN
            return res
    if request.method == 'GET':
        try:
            ctrl = DispatchController()
            retData = ctrl.getDispatch(request)
            result = DispatchSerializer(retData).data
            return HttpResponse(JSONRenderer().render(result))
        except Exception,e:
            from rest_framework import status
            res = HttpResponse(e)
            res.status_code = status.HTTP_403_FORBIDDEN
            return res

    if request.method == 'PUT':
        try:
            ctrl = DispatchController()
            retData = ctrl.updateDispatch(request)
            result = DispatchSerializer(retData).data
            return HttpResponse(JSONRenderer().render(result))
        except Exception,e:
            from rest_framework import status
            res = HttpResponse(e)
            res.status_code = status.HTTP_403_FORBIDDEN
            return res



@api_view(['GET'])
def dispatches(request,**args):
    try:
        # return HttpResponse('result')
        ctrl = DispatchController()
        retData = ctrl.getDispatches(request)
        result = DispatchSerializer(retData,many=True).data
        return HttpResponse(JSONRenderer().render(result))
    except Exception,e:

        from rest_framework import status
        res = HttpResponse(e)
        res.status_code = status.HTTP_403_FORBIDDEN
        return res

@api_view(['GET'])
def vans(request,**args):
    try:
        # return HttpResponse('result')
        ctrl = DispatchController()
        retData = ctrl.getVans()
        return HttpResponse(JSONRenderer().render(retData))
    except Exception,e:

        from rest_framework import status
        res = HttpResponse(e)
        res.status_code = status.HTTP_403_FORBIDDEN
        return res


@api_view(['GET'])
def forwardingnote(request,**args):
    try:
        # return HttpResponse('result')
        ctrl = ForwardingController()
        retData = ctrl.getForwardingNote(request)
        result = ForwardingSerializer(retData,many=True).data
        return HttpResponse(JSONRenderer().render(result))
    except Exception,e:

        from rest_framework import status
        res = HttpResponse(e)
        res.status_code = status.HTTP_403_FORBIDDEN
        return res



    # if request.user.is_authenticated():
    #     requestArr = request.path.split('/')
    #     reqType = getArrIdx(requestArr, 2)
    #     if reqType == api:
    #         return handleApiRequest(request, **arg)
    # else:
    #     dict = {}
    #     dict['status'] = 'error'
    #     dict['message'] = UNAUTHORISED_MESSAGE