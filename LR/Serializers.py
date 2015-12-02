from rest_framework import serializers
from LR.models import Transporter,Customer,ForwardingNote,Dispatch,Station,Company
class StationsSeializers(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = ('label')
class TransporterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transporter
        fields = ('stations','label','id','name','contactNumber','contactPerson','isActive','addressLine1','addressLine2','area','city','state','country')
        depth = 1

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('label','id','name','org','contactPerson','contactNumber','isActive','addressLine1','addressLine2','area','city','state','country')


class ForwardingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForwardingNote
        fields = ('id','billDates','transporter','customer','createdDate','billNo','billValues','cases','marka','permitNo','consignor','comments','isDispatched')

class ForwardingDetailSerializer(serializers.ModelSerializer):
    transporter = TransporterSerializer()
    customer = CustomerSerializer()
    class Meta:
        model = ForwardingNote
        fields = ('fnDate','id','billDates','transporter','customer','createdDate','billNo','billValues','cases','marka','permitNo','consignor','comments','isDispatched')


class DispatchSerializer(serializers.ModelSerializer):
    forwardingNote = ForwardingDetailSerializer(many=True)
    class Meta:
        model = Dispatch
        fields = ('id','date','vanNo','name','remarks','forwardingNote')


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id','label','code')

