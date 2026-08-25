from LR.models import Transporter


class TransporterController:
    def getTransporters(self, requestUser):
        return (
            Transporter.objects.filter(isActive=True)
            .prefetch_related('stations')
            .order_by('name')
        )
