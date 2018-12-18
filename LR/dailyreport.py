from django.shortcuts import render
import re,json
from constants import BRANCHES
from django.shortcuts import redirect
from django.db.models import Sum
from datetime import datetime
from  django.http import HttpResponse
from LR.models import DailyReport
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from LR.Serializers import DailyReportSerializer

def to_snake_case(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

class CheckEntryView(APIView):
    def get(self,request):
        data=request.query_params
        branch_name=data.get("branchname")
        date=data.get("date")
        try:
            obj=DailyReport.objects.get(branch_name=branch_name,date=date)
            if obj.is_editable:
                stat = status.HTTP_200_OK
                serializer=DailyReportSerializer(obj)
                return Response(serializer.data, status=stat)
            else:
                stat = status.HTTP_403_FORBIDDEN
        except DailyReport.DoesNotExist:
            stat=status.HTTP_200_OK
        return Response({},status=stat)

def chartView(request):
    context={}
    if request.method=="GET":
        start_date=request.GET.get('start_date',datetime.strftime(datetime.today(),"%Y-%m-%d"))
        end_date=request.GET.get('end_date',datetime.strftime(datetime.today(),"%Y-%m-%d"))
        filterParams={}
        filterParams["date__gte"] = start_date
        filterParams["date__lte"] = end_date
        if request.GET.get("branch") and not request.GET.get("branch")=="All":
            filterParams["branch_name"] =request.GET.get("branch")
        data=DailyReport.objects.filter(**filterParams).aggregate(Sum("day_card_sale")
        ,Sum("day_credit_sale"),Sum("day_cash_sale"),
        Sum("total_credit_purchase"),Sum("total_cash_purchase"),
        Sum("bank_deposit"),
        Sum("total_expense"),
        Sum("total_misc_cash_in")
).values()
        data.insert(3,sum(data[0:3]))
        data.insert(6,sum(data[4:6]))
        context['data']=data
        context['branches'] = BRANCHES
    return render(request,"chart.html",context)
def dailyReportView(request):
    context={}
    if request.method=="POST" and request.is_ajax():
        data = request.POST.get("data")
        data=json.loads(data)
        camel={}
        for i in data.keys():
            value=data[i]
            if 'detail' in i.lower():
                value=json.dumps(value)
            camel[to_snake_case(i)]=value if value else 0
        try:
            obj = DailyReport.objects.get(branch_name=data.get("BranchName"), date=data.get("Date"))
            if not obj.is_editable:
                return redirect('/dailyreport/')
        except DailyReport.DoesNotExist:
            pass
        if 'edit' in request.POST:
            obj=DailyReport.objects.get(branch_name=data.get("BranchName"),date=data.get("Date"))
            camel["is_editable"]=False
            serializer=DailyReportSerializer(obj,data=camel)
        else:
            serializer = DailyReportSerializer(data=camel)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(serializer.data)
        else:
            return HttpResponse(serializer.errors)

        return HttpResponse("Daily Report Created")

    if request.method == "GET":
        #Add branches here
        context['branches']= BRANCHES
    return render(request, 'dailyreport.html', context)
