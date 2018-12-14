from LR.models import DailyReport
from rest_framework.serializers import ModelSerializer
class DailyReportSerializer(ModelSerializer):
    class Meta:
        model=DailyReport
        fields="__all__"
