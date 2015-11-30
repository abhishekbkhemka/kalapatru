from django.shortcuts import render
from rest_framework.decorators import api_view
from LR.TransporterCtl import TransporterController
from LR.CustomerCtl import CustomerController
from LR.ForwardingController import ForwardingController
from LR.DispatchController import DispatchController
from django.http import HttpResponse
from LR.Serializers import TransporterSerializer,CustomerSerializer,ForwardingSerializer,DispatchSerializer,ForwardingDetailSerializer,CompanySerializer
from rest_framework.renderers import JSONRenderer




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
def companies(request, **arg):
    try:
        ctrl = ForwardingController()
        retData = ctrl.getCompanies(request)
        result = CompanySerializer(retData,many=True).data
        return HttpResponse(JSONRenderer().render(result))
    except Exception,e:
        from rest_framework import status
        res = HttpResponse(e)
        res.status_code = status.HTTP_403_FORBIDDEN
        return res

@api_view(['POST'])
def forwardingNote(request,**args):
    try:
        ctrl = ForwardingController()
        retData = ctrl.addForwardingNote(request)
        result = ForwardingSerializer(retData).data
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


@api_view(['POST'])
def dispatch(request,**args):
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






    # if request.user.is_authenticated():
    #     requestArr = request.path.split('/')
    #     reqType = getArrIdx(requestArr, 2)
    #     if reqType == api:
    #         return handleApiRequest(request, **arg)
    # else:
    #     dict = {}
    #     dict['status'] = 'error'
    #     dict['message'] = UNAUTHORISED_MESSAGE