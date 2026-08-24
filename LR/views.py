from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status

from LR.TransporterCtl import TransporterController
from LR.CustomerCtl import CustomerController
from LR.ForwardingController import ForwardingController
from LR.DispatchController import DispatchController
from LR.Serializers import (
    TransporterSerializer,
    StationsSeializers,
    CustomerSerializer,
    ForwardingSerializer,
    DispatchSerializer,
    ForwardingDetailSerializer,
    CompanySerializer,
    CommoditySeializers,
)
from accounts.permissions import IsAuthenticatedActive, ReadOnlyOrOperator


@api_view(['GET'])
@permission_classes([IsAuthenticatedActive])
def transporters(request, **arg):
    try:
        ctrl = TransporterController()
        retData = ctrl.getTransporters(request.user)
        result = TransporterSerializer(retData, many=True).data
        return Response(result)
    except Exception as e:
        return Response(str(e), status=status.HTTP_403_FORBIDDEN)


@api_view(['GET'])
@permission_classes([IsAuthenticatedActive])
def customers(request, **arg):
    try:
        ctrl = CustomerController()
        retData = ctrl.getCustomers(request.user)
        result = CustomerSerializer(retData, many=True).data
        return Response(result)
    except Exception as e:
        return Response(str(e), status=status.HTTP_403_FORBIDDEN)


@api_view(['GET'])
@permission_classes([IsAuthenticatedActive])
def settings(request, **arg):
    try:
        ctrl = ForwardingController()
        companies, commodity, stations = ctrl.getSettings(request)
        result = {
            'companies': CompanySerializer(companies, many=True).data,
            'commodities': CommoditySeializers(commodity, many=True).data,
            'stations': StationsSeializers(stations, many=True).data,
        }
        return Response(result)
    except Exception as e:
        return Response(str(e), status=status.HTTP_403_FORBIDDEN)


@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticatedActive, ReadOnlyOrOperator])
def forwardingNote(request, **args):
    try:
        if request.method == 'POST':
            ctrl = ForwardingController()
            retData = ctrl.addForwardingNote(request)
            return Response(ForwardingSerializer(retData).data)

        if request.method == 'GET':
            ctrl = ForwardingController()
            retData = ctrl.getForwardingNote(request)
            return Response(ForwardingDetailSerializer(retData).data)
    except Exception as e:
        return Response(str(e), status=status.HTTP_403_FORBIDDEN)


@api_view(['GET'])
@permission_classes([IsAuthenticatedActive])
def forwardingNotes(request, **args):
    try:
        ctrl = ForwardingController()
        retData = ctrl.getForwardingNotes(request)
        return Response(ForwardingDetailSerializer(retData, many=True).data)
    except Exception as e:
        return Response(str(e), status=status.HTTP_403_FORBIDDEN)


@api_view(['POST', 'GET', 'PUT'])
@permission_classes([IsAuthenticatedActive, ReadOnlyOrOperator])
def dispatch(request, **args):
    try:
        ctrl = DispatchController()
        if request.method == 'POST':
            retData = ctrl.addDispatch(request)
            return Response(DispatchSerializer(retData).data)
        if request.method == 'GET':
            retData = ctrl.getDispatch(request)
            return Response(DispatchSerializer(retData).data)
        if request.method == 'PUT':
            retData = ctrl.updateDispatch(request)
            return Response(DispatchSerializer(retData).data)
    except Exception as e:
        return Response(str(e), status=status.HTTP_403_FORBIDDEN)


@api_view(['GET'])
@permission_classes([IsAuthenticatedActive])
def dispatches(request, **args):
    try:
        ctrl = DispatchController()
        retData = ctrl.getDispatches(request)
        return Response(DispatchSerializer(retData, many=True).data)
    except Exception as e:
        return Response(str(e), status=status.HTTP_403_FORBIDDEN)


@api_view(['GET'])
@permission_classes([IsAuthenticatedActive])
def vans(request, **args):
    try:
        ctrl = DispatchController()
        retData = ctrl.getVans()
        return Response(retData)
    except Exception as e:
        return Response(str(e), status=status.HTTP_403_FORBIDDEN)
