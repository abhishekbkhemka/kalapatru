
from LR.models import Transporter
class TransporterController():

    def getTransporters(self,requestUser):
        transporters = Transporter.objects.filter().order_by('name')
        return transporters