
from LR.models import Transporter
class TransporterController():

    def getTransporters(self,requestUser):
        transporters = Transporter.objects.filter(isActive=True).order_by('name')
        return transporters