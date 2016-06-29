from LR.models import Transporter


def migrateData():
    mapDict = {}
    transObj=Transporter.objects.all()
    for obj in transObj:
        if not str(obj.name) in mapDict:
            obj.isActive=True
            obj.save()
            mapDict[name] = True

